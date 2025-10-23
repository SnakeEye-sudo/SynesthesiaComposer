import streamlit as st
import numpy as np
from PIL import Image
import json
import os

# Page configuration
st.set_page_config(
    page_title="SynesthesiaComposer",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for storing compositions
if 'compositions' not in st.session_state:
    st.session_state.compositions = []

if 'current_input' not in st.session_state:
    st.session_state.current_input = None

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4ECDC4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #F7F7F7;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
        margin: 10px 0;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Main page content
st.markdown('<div class="main-header">🎵 SynesthesiaComposer 🎨</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Transform Sensory Experiences into Musical Compositions</div>', unsafe_allow_html=True)

# Introduction section
st.markdown("""
<div class="info-box">
    <h2>🌈 What is Synesthesia?</h2>
    <p>
        Synesthesia is a fascinating neurological phenomenon where stimulation of one sensory pathway 
        leads to automatic, involuntary experiences in another sensory pathway. For example, some people 
        might "see" colors when they hear music, or "taste" shapes.
    </p>
    <p>
        <strong>SynesthesiaComposer</strong> brings this concept to life by allowing you to transform 
        various sensory inputs (colors, images, text, emotions) into unique musical compositions.
    </p>
</div>
""", unsafe_allow_html=True)

# Features section
st.markdown("## ✨ Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🎨 InputSense</h3>
        <p>Capture and process various sensory inputs:</p>
        <ul>
            <li>Color to music mapping</li>
            <li>Image analysis for composition</li>
            <li>Text sentiment to melody</li>
            <li>Emotion-based generation</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🎼 ComposeMusic</h3>
        <p>Advanced music generation engine that:</p>
        <ul>
            <li>Converts sensory data to MIDI</li>
            <li>Applies musical theory rules</li>
            <li>Creates harmonious compositions</li>
            <li>Exports in multiple formats</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📚 MyLibrary</h3>
        <p>Personal composition management:</p>
        <ul>
            <li>Save your creations</li>
            <li>Organize by categories</li>
            <li>Replay compositions</li>
            <li>Export and share</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🔧 Technology Stack</h3>
        <ul>
            <li>Streamlit - Web framework</li>
            <li>Music21 - Music generation</li>
            <li>NumPy/Pandas - Data processing</li>
            <li>Pillow - Image processing</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# How it works section
st.markdown("## 🚀 How It Works")

st.markdown("""
<div class="info-box">
    <ol>
        <li><strong>Input:</strong> Navigate to the <em>InputSense</em> page and provide your sensory input (color, image, text, or emotion)</li>
        <li><strong>Process:</strong> Our algorithms analyze your input and map it to musical parameters (pitch, rhythm, harmony, tempo)</li>
        <li><strong>Compose:</strong> Go to <em>ComposeMusic</em> to generate your unique musical piece</li>
        <li><strong>Save:</strong> Store your compositions in <em>MyLibrary</em> for future listening and sharing</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Getting started section
st.markdown("## 🎯 Getting Started")

st.info("""
👉 **Ready to create your first synesthetic composition?**

1. Click on **InputSense** in the sidebar to provide your sensory input
2. Explore different input types to see how they translate to music
3. Visit **ComposeMusic** to generate and customize your composition
4. Save your favorites in **MyLibrary**

Let your senses guide the music! 🎵✨
""")

# Sidebar content
with st.sidebar:
    st.markdown("### 📊 Session Info")
    st.write(f"Compositions created: {len(st.session_state.compositions)}")
    
    if st.session_state.current_input:
        st.success("✅ Current input ready for composition")
    else:
        st.warning("⚠️ No input selected yet")
    
    st.markdown("---")
    st.markdown("""
    ### 🎓 Quick Tips
    - Bright colors → Higher pitches
    - Dark colors → Lower pitches
    - Warm colors → Major keys
    - Cool colors → Minor keys
    - Complex images → Rich harmonies
    """)
    
    st.markdown("---")
    st.markdown("""
    ### 📖 About
    Created with ❤️ for music and technology enthusiasts.
    
    Explore the fascinating intersection of sensory perception and musical creativity!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888;'>
    <p>SynesthesiaComposer v1.0 | MIT License | 2025</p>
</div>
""", unsafe_allow_html=True)
