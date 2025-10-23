# SynesthesiaComposer

A Streamlit application that transforms sensory input into musical compositions using synesthesia principles.

## Overview

SynesthesiaComposer is an innovative music creation tool that leverages the concept of synesthesia - the neurological phenomenon where stimulation of one sensory pathway leads to automatic experiences in another sensory pathway. This application allows users to input various sensory data (colors, images, text, emotions) and converts them into musical compositions.

## Features

- **Home**: Introduction to the application and synesthesia concepts
- **InputSense**: Interface for capturing and processing various sensory inputs
  - Color-to-music mapping
  - Image analysis for musical generation
  - Text sentiment to melody conversion
  - Emotion-based composition
- **ComposeMusic**: Music generation engine that transforms sensory data into MIDI compositions
- **MyLibrary**: Personal library to save, organize, and replay your created compositions

## Technology Stack

- **Streamlit**: Web application framework
- **Python**: Core programming language
- **Music21**: Music analysis and generation
- **NumPy/Pandas**: Data processing
- **Pillow**: Image processing

## Installation

```bash
pip install streamlit music21 numpy pandas pillow
```

## Usage

```bash
streamlit run app.py
```

## Project Structure

```
SynesthesiaComposer/
├── app.py                 # Main application file
├── pages/
│   ├── 1_InputSense.py   # Input processing page
│   ├── 2_ComposeMusic.py # Music composition page
│   └── 3_MyLibrary.py    # Library management page
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## License

MIT License

## Author

Created with passion for music and technology
