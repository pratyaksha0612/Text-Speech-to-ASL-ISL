# VYAKT: Sign Language Translation Ecosystem

VYAKT is an intelligent, visual communication platform designed to bridge the gap between spoken/written language and sign systems. By translating text and real-time speech into sign language sequences, VYAKT makes digital communication accessible, inclusive, and natural.

The platform supports American Sign Language (ASL) and Indian Sign Language (ISL).

# Key Features

* Dual Sign Portals: Dedicated portals for American Sign Language (ASL) and Indian Sign Language (ISL).
* Text to Sign Translation: Convert typed text into seamless sign language video sequences.
* Speech to Sign Translation: Utilize real-time voice-to-text recognition to render spoken words into sign language.
* Speed Control: Customize video playback speeds from 0.25x up to 2.00x for individualized learning and natural pacing.
* Interactive A to Z Reference: Hover-to-preview and click-to-replay reference video grids for both ASL and ISL letters.
* Centered Video Playback: Clean, screen-centered modal popups for clear video viewing.
* Ashi Conversational Assistant: A multilingual AI assistant styled as a floating avatar with interactive orbit text and contextual guidance.
* Portal Navigation: Integrated back-navigation buttons allowing quick switching between text/speech options and portal choices.

# Architecture & Technology Stack

* Backend Framework: Python, Flask
* Frontend: HTML5, CSS3, JavaScript (ES6)
* Visual Effects: Dynamic 3D Starfield Canvas and Responsive Glassmorphism Styling
* Speech Recognition Engine: Web Speech API for real-time browser audio processing

# Installation and Setup

### Prerequisites

Ensure Python 3.8 or higher is installed. Install required Python packages:

```bash
pip install flask gunicorn
```

### Running the Application

1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to:
   ```text
   http://127.0.0.1:5000
   ```

# Project Structure

* `app.py`: Core Flask application routes and API endpoints.
* `texttoasl.py`: ASL text translation engine.
* `texttoisl.py`: ISL text translation engine.
* `speechtoasl.py`: ASL speech translation engine interface.
* `speechtoisl.py`: ISL speech translation engine interface.
* `templates/`: HTML templates for portals, translation pages, and Ashi assistant.
* `static/`: Styling, JavaScript, brand logos, avatar graphics, and base videos.
* `dataset/`: Comprehensive video datasets for ASL and ISL sign letters.

# Author

* Pratyaksha Singh
* VIT Bhopal University

# License

This project is licensed under the MIT License.
