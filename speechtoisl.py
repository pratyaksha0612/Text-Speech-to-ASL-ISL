import os
import cv2
import time
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile

# Global recording vars
fs = 44100
duration = 0
recording = None
recording_file = None

isl_dataset_path = "C:/Users/Chhavi/Desktop/text-speech-to-sign/dataset/isl"
black_video_path = "static/blank.mp4"
resize_ratio = 0.5

# Consistent, always-on-top window name
window_name = "ISL Translator"

def play_video(video_path, resize=True):
    if not os.path.exists(video_path):
        print(f"❌ Video not found at: {video_path}")
        return False

    cap = cv2.VideoCapture(video_path)

    # Ensure the window pops up and stays on top
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if resize:
            height, width = frame.shape[:2]
            frame = cv2.resize(frame, (int(width * resize_ratio), int(height * resize_ratio)))
        cv2.imshow(window_name, frame)

        # Exit on 'q'
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    return True

def display_sign_video(letter):
    video_path = os.path.join(isl_dataset_path, f"{letter.lower()}.mp4")
    if os.path.exists(video_path):
        return play_video(video_path)
    return False

def display_black():
    if os.path.exists(black_video_path):
        return play_video(black_video_path, resize=False)
    return False

# 🎤 Start Recording
def isl_start_recording():
    global recording, recording_file
    print("🎙️ Start recording...")
    recording = sd.rec(int(10 * fs), samplerate=fs, channels=1, dtype='int16')  # Max 10s buffer
    recording_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    return "Recording started"

# 🛑 Stop Recording & Translate
def isl_stop_and_translate():
    global recording, recording_file
    print("🛑 Stopping recording...")
    sd.stop()
    write(recording_file.name, fs, recording)
    return isl_translate_audio(recording_file.name)

def isl_translate_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 Recognized: {text}")
        process_text(text)
        return text
    except Exception as e:
        print(f"Error: {e}")
        return ""

def process_text(text):
    for char in text:
        if char.isalpha():
            if not display_sign_video(char):
                break
            time.sleep(0.5)
        elif char == " ":
            if not display_black():
                break
            time.sleep(0.5)
    cv2.destroyAllWindows()
