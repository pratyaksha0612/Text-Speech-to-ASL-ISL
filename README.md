# Vyakta - Text and Speech to Sign Language Translator

**Vyakta (व्यक्त)** is a Sanskrit word meaning **"expressed"** or **"made visible."**  
This project embodies that meaning by converting **text and speech into visual sign language**, enabling communication accessibility through expression.

Vyakta is a web-based application that translates **Text and Speech into Indian Sign Language (ISL) and American Sign Language (ASL)** using real sign language video playback.

It is designed to support accessibility, assist learning, and bridge communication gaps between the hearing and the deaf community.



# Demo

A demonstration of the project is available in:



# Features

• Supports both **Indian Sign Language (ISL)** and **American Sign Language (ASL)**

• Accepts:

- Text input  
- Speech input  

• Converts speech to text using speech recognition

• Displays **real sign language videos**

• Smooth continuous playback in a single window

• Handles:

- Words  
- Sentences  
- Spaces  

• Modern, dynamic web interface



# How It Works

1. User opens the Vyakta web application

2. Selects preferred sign language:

   - ISL  
   - ASL  

3. Provides input:

   - Text  
   OR  
   - Speech  

4. If speech is provided, system converts speech → text

5. Text is split into characters

6. Corresponding sign language videos are played sequentially



# Project Structure

Vyakta/
│
├── app.py
│
├── speechtoasl.py
├── speechtoisl.py
│
├── texttoasl.py
├── texttoisl.py
│
├── dataset/
│ ├── asl/
│ └── isl/
│
├── static/
│ ├── style.css
│ ├── logo-main.png
│ ├── logo-nav.png
│ ├── logo-hero.png
│ ├── blank.mp4
│
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── about.html
│ ├── asl.html
│ ├── isl.html
│ ├── asl_text.html
│ ├── asl_speech.html
│ ├── isl_text.html
│ ├── isl_speech.html
│
└── DEMO.mp4



# Installation

## Step 1 — Clone Repository

git clone https://github.com/pratyaksha0612/Text-Speech-to-ASL-ISL.git

cd Text-Speech-to-ASL-ISL




## Step 2 — Install Dependencies

pip install flask
pip install opencv-python
pip install sounddevice
pip install scipy
pip install SpeechRecognition




# Running the Application

python app.py


Open browser and go to:

http://127.0.0.1:5000/




# Technologies Used

Python  
Flask  
OpenCV  
SpeechRecognition  
HTML  
CSS  
JavaScript  



# Purpose

Vyakta aims to:

• Make communication accessible

• Enable sign language learning

• Assist deaf-mute communication

• Convert speech into visual expression



# Meaning of Name

**Vyakta (व्यक्त)**

Meaning:

Expressed  
Manifested  
Made visible  

This reflects the core goal of the project:

Converting speech and text into visible communication.



# Future Improvements

• Word-level translation

• Sentence-level translation

• Real-time sign recognition

• Deep learning integration

• Mobile application version



# Author

Pratyaksha Singh  
B.Tech CSE — AI & ML  
VIT Bhopal University



# License

MIT License
