import streamlit as st
import numpy as np
from PIL import Image, ImageStat
import colorsys
import json

# Page configuration
st.set_page_config(
    page_title="InputSense - SynesthesiaComposer",
    page_icon="🎨",
    layout="wide"
)

# Title
st.title("🎨 InputSense: Capture Your Sensory Input")
st.markdown("Transform your sensory experiences into data ready for musical composition.")

# Tabs for different input types
input_tab1, input_tab2, input_tab3, input_tab4 = st.tabs([
    "🌈 Color Input", 
    "🖼️ Image Input", 
    "📝 Text Input", 
    "💖 Emotion Input"
])

# Color Input Tab
with input_tab1:
    st.header("Color to Music Mapping")
    st.markdown("""
    Colors evoke different musical qualities:
    - **Hue** → Pitch (Red=Low, Violet=High)
    - **Saturation** → Intensity/Volume
    - **Brightness** → Tempo
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        color_input = st.color_picker("Pick a color", "#FF6B6B")
        st.markdown(f"**Selected Color:** {color_input}")
        
        # Convert hex to RGB
        rgb = tuple(int(color_input[i:i+2], 16) for i in (1, 3, 5))
        st.write(f"RGB: {rgb}")
        
        # Convert to HSV
        hsv = colorsys.rgb_to_hsv(rgb[0]/255, rgb[1]/255, rgb[2]/255)
        st.write(f"HSV: H={hsv[0]:.2f}, S={hsv[1]:.2f}, V={hsv[2]:.2f}")
    
    with col2:
        st.markdown("### Musical Mapping")
        
        # Map hue to note (0-1 maps to C-B)
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        note_index = int(hsv[0] * 12) % 12
        note = notes[note_index]
        
        # Map saturation to intensity
        intensity = "Low" if hsv[1] < 0.3 else "Medium" if hsv[1] < 0.7 else "High"
        
        # Map value/brightness to tempo
        tempo = int(60 + hsv[2] * 120)  # Range: 60-180 BPM
        
        st.info(f"""
        🎵 **Musical Parameters:**
        - Base Note: **{note}**
        - Intensity: **{intensity}**
        - Tempo: **{tempo} BPM**
        """)
        
        if st.button("Save Color Input", key="save_color"):
            st.session_state.current_input = {
                'type': 'color',
                'data': {
                    'hex': color_input,
                    'rgb': rgb,
                    'hsv': hsv,
                    'note': note,
                    'intensity': intensity,
                    'tempo': tempo
                }
            }
            st.success("✅ Color input saved! Go to ComposeMusic to generate your composition.")

# Image Input Tab
with input_tab2:
    st.header("Image to Music Conversion")
    st.markdown("""
    Upload an image and we'll analyze its visual properties to create music:
    - **Dominant colors** → Chord progressions
    - **Brightness distribution** → Dynamics
    - **Complexity** → Rhythm patterns
    """)
    
    uploaded_image = st.file_uploader("Choose an image", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_image:
        col1, col2 = st.columns(2)
        
        with col1:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_container_width=True)
        
        with col2:
            st.markdown("### Image Analysis")
            
            # Get image statistics
            stat = ImageStat.Stat(image)
            
            # Average RGB
            avg_rgb = stat.mean[:3] if len(stat.mean) >= 3 else stat.mean
            st.write(f"Average RGB: {tuple(int(x) for x in avg_rgb)}")
            
            # Brightness
            brightness = sum(avg_rgb) / (3 * 255)
            st.write(f"Brightness: {brightness:.2f}")
            
            # Image complexity (standard deviation as proxy)
            complexity = sum(stat.stddev[:3]) / (3 * 255) if len(stat.stddev) >= 3 else 0
            st.write(f"Complexity: {complexity:.2f}")
            
            st.info(f"""
            🎶 **Musical Interpretation:**
            - Mood: **{'Bright/Major' if brightness > 0.5 else 'Dark/Minor'}**
            - Complexity: **{'High' if complexity > 0.3 else 'Low'}**
            - Dynamics: **{'Forte' if brightness > 0.7 else 'Piano'}**
            """)
            
            if st.button("Save Image Input", key="save_image"):
                st.session_state.current_input = {
                    'type': 'image',
                    'data': {
                        'avg_rgb': avg_rgb,
                        'brightness': brightness,
                        'complexity': complexity,
                        'size': image.size
                    }
                }
                st.success("✅ Image input saved! Go to ComposeMusic to generate your composition.")

# Text Input Tab
with input_tab3:
    st.header("Text to Melody Conversion")
    st.markdown("""
    Enter text and we'll analyze its sentiment and structure to create music:
    - **Sentiment** → Major/Minor key
    - **Word length** → Note duration
    - **Punctuation** → Rests and pauses
    """)
    
    text_input = st.text_area("Enter your text", height=150, 
                              placeholder="Type something meaningful...")
    
    if text_input:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Text Analysis")
            
            word_count = len(text_input.split())
            char_count = len(text_input)
            avg_word_length = char_count / word_count if word_count > 0 else 0
            
            st.write(f"Word Count: {word_count}")
            st.write(f"Character Count: {char_count}")
            st.write(f"Average Word Length: {avg_word_length:.2f}")
            
            # Simple sentiment analysis based on word characteristics
            exclamation_count = text_input.count('!')
            question_count = text_input.count('?')
            uppercase_ratio = sum(1 for c in text_input if c.isupper()) / char_count if char_count > 0 else 0
            
            st.write(f"Exclamations: {exclamation_count}")
            st.write(f"Questions: {question_count}")
            st.write(f"Uppercase Ratio: {uppercase_ratio:.2%}")
        
        with col2:
            st.markdown("### Musical Interpretation")
            
            # Determine mood
            energy_level = exclamation_count + uppercase_ratio * 10
            mood = "Energetic" if energy_level > 2 else "Calm"
            
            # Determine key
            key_type = "Major" if exclamation_count > question_count else "Minor"
            
            # Determine tempo
            tempo = int(90 + min(energy_level * 10, 60))
            
            st.info(f"""
            🎵 **Musical Parameters:**
            - Mood: **{mood}**
            - Key: **{key_type}**
            - Tempo: **{tempo} BPM**
            - Measures: **{min(word_count // 4, 16)}**
            """)
            
            if st.button("Save Text Input", key="save_text"):
                st.session_state.current_input = {
                    'type': 'text',
                    'data': {
                        'text': text_input[:200],  # Store first 200 chars
                        'word_count': word_count,
                        'mood': mood,
                        'key': key_type,
                        'tempo': tempo
                    }
                }
                st.success("✅ Text input saved! Go to ComposeMusic to generate your composition.")

# Emotion Input Tab
with input_tab4:
    st.header("Emotion to Music Mapping")
    st.markdown("""
    Select emotions and their intensities to create music that matches your feelings.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Select Your Emotions")
        
        emotion_joy = st.slider("Joy 😊", 0, 100, 50)
        emotion_sadness = st.slider("Sadness 😢", 0, 100, 20)
        emotion_energy = st.slider("Energy ⚡", 0, 100, 60)
        emotion_calm = st.slider("Calm 🧘", 0, 100, 40)
        
    with col2:
        st.markdown("### Musical Mapping")
        
        # Calculate musical parameters from emotions
        valence = (emotion_joy - emotion_sadness) / 100
        arousal = (emotion_energy - emotion_calm) / 100
        
        # Determine key
        key = "Major" if valence > 0 else "Minor"
        
        # Determine tempo (based on arousal)
        tempo = int(80 + arousal * 60)
        
        # Determine mode
        if valence > 0 and arousal > 0:
            mood = "Happy & Energetic"
            scale = "Major Pentatonic"
        elif valence > 0 and arousal < 0:
            mood = "Content & Peaceful"
            scale = "Major"
        elif valence < 0 and arousal > 0:
            mood = "Anxious & Tense"
            scale = "Phrygian"
        else:
            mood = "Melancholic & Slow"
            scale = "Minor"
        
        st.info(f"""
        🎶 **Musical Parameters:**
        - Mood: **{mood}**
        - Key: **{key}**
        - Scale: **{scale}**
        - Tempo: **{tempo} BPM**
        """)
        
        if st.button("Save Emotion Input", key="save_emotion"):
            st.session_state.current_input = {
                'type': 'emotion',
                'data': {
                    'joy': emotion_joy,
                    'sadness': emotion_sadness,
                    'energy': emotion_energy,
                    'calm': emotion_calm,
                    'valence': valence,
                    'arousal': arousal,
                    'mood': mood,
                    'key': key,
                    'scale': scale,
                    'tempo': tempo
                }
            }
            st.success("✅ Emotion input saved! Go to ComposeMusic to generate your composition.")

# Sidebar
with st.sidebar:
    st.markdown("### 📊 Current Session")
    
    if st.session_state.current_input:
        input_type = st.session_state.current_input['type']
        st.success(f"✅ {input_type.capitalize()} input ready")
        
        if st.button("🗑️ Clear Input"):
            st.session_state.current_input = None
            st.rerun()
    else:
        st.info("ℹ️ No input selected yet")
    
    st.markdown("---")
    st.markdown("""
    ### 💡 Tips
    - Try different input types to explore various musical styles
    - Bright colors and happy emotions create uplifting music
    - Complex images generate richer harmonies
    - Text with more exclamation points creates energetic compositions
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
    <p>Choose your input type above, then proceed to <strong>ComposeMusic</strong> to generate your composition!</p>
</div>
""", unsafe_allow_html=True)
