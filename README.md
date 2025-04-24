# Text and Speech to ASL/ISL Translator

This project is a web-based application that facilitates communication by converting both **text** and **speech input** into **American Sign Language (ASL)** or **Indian Sign Language (ISL)**. The goal of this project is to provide an intuitive platform for the deaf and hard-of-hearing community by translating written or spoken English into corresponding sign language via video playback.

## Project Description

The user begins by selecting their preferred sign language mode — either **ASL** or **ISL** — from the homepage. Afterward, the user can either:

- **Enter text input**: The user types in a word, letter, or full sentence.
- **Provide speech input**: The system transcribes speech into text using speech recognition.

### Current Implementation

- **Spelling Out Words**: All words are spelled out letter by letter using pre-recorded **A–Z sign language videos**. If a word is provided as input, each letter of the word is shown sequentially.
- **Blank Handling**: If the input is blank or unrecognized, a **black screen** is displayed, and the system proceeds to the next word.
- **Sentence Handling**: Sentences are split into words, and each word is spelled out using the alphabet.

## Features

- User can select between **ASL** and **ISL** modes.
- Dual input support for **Text** and **Speech**.
- **Real-time video playback** for each letter in a word.
- Automatic handling of blank inputs or unsupported words with a black screen.
- **Text-to-speech** functionality for added accessibility and feedback.

## Project Structure

```
Text-Speech-to-ASL-ISL/
├── app.py                     # Flask server application
├── templates/
│   └── index.html             # Main user interface
├── static/
│   ├── style.css              # Application styling
│   └── video_display.js       # JavaScript for handling video sequencing
├── dataset/
│   ├── asl/                   # ASL A–Z sign videos (a.mp4, b.mp4, ...)
│   └── isl/                   # ISL A–Z sign videos (a.mp4, b.mp4, ...)
├── labels.csv                 # Mapping of words to video paths
└── wlasl.json                 # Video ID mapping for WLASL dataset
```


## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/pratyaksha0612/Text-Speech-to-ASL-ISL.git
cd Text-Speech-to-ASL-ISL
```

### Step 2: Install Dependencies

Ensure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

> Note: This application requires `ffmpeg` to be installed and added to your system path (used by moviepy).

## Running the Application

```bash
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000/
```


## How It Works

1. The user selects either ASL or ISL mode.
2. The user provides input via text or speech.
3. If the input is a word, the system spells it out letter by letter using corresponding sign language videos.
4. If the input is blank or unrecognized, a black screen is shown, and the system proceeds to the next word.
5. The system continues by displaying sign videos for each letter in the next word or phrase.

## Dataset Credits

- **ASL Dataset**: Derived from educational sign videos  
  Source: [ASL Alphabet Sign Language](https://youtu.be/DBQINq0SsAw?si=J802HVMhR6SAe0sX)

- **ISL Dataset**: Extracted from tutorial footage for Indian Sign Language  
  Source: [ISL Alphabet Signs](https://youtu.be/qcdivQfA41Y?si=qTzoJTMSPW8tIIpG)


## Demo Video



## Future Enhancements

- Expand the system to handle complete words and phrases for ASL/ISL.
- Incorporate real-time gesture recognition to support sign-to-text translation.
- Enhance the performance for low-resource devices.
- Improve UI/UX design for better accessibility and interactivity.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for full terms.
