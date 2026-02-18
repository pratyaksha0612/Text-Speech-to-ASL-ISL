import os
import cv2
import ctypes
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import tempfile

# Recording settings
fs = 44100
recording = None
recording_file = None

asl_dataset_path = "C:\\Users\\PRATYAKSHA SINGH\\OneDrive\\Desktop\\COLLEGE\\PROJECTS\\Text-Speech-to-ASL-ISL\\dataset\\asl"
black_video_path = "static/blank.mp4"

window_name = "ASL Translator"


def get_screen_size():

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()

    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def play_text_videos(text):

    screen_width, screen_height = get_screen_size()

    window_size = int(min(screen_width, screen_height) * 0.60)

    x = (screen_width - window_size) // 2
    y = (screen_height - window_size) // 2

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, window_size, window_size)
    cv2.moveWindow(window_name, x, y)

    cv2.setWindowProperty(window_name, cv2.WND_PROP_TOPMOST, 1)


    for char in text:

        if char.isalpha():

            video_path = os.path.join(asl_dataset_path, f"{char.lower()}.mp4")

        elif char == " ":

            video_path = black_video_path

        else:
            continue


        if not os.path.exists(video_path):

            print("❌ Video not found:", video_path)

            continue


        cap = cv2.VideoCapture(video_path)


        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break

            frame = cv2.resize(frame, (window_size, window_size))

            cv2.imshow(window_name, frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


        cap.release()


    cv2.destroyAllWindows()


# Start recording
def asl_start_recording():

    global recording, recording_file

    print("🎙️ Start recording...")

    recording = sd.rec(int(10 * fs), samplerate=fs, channels=1, dtype='int16')

    recording_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")

    return "Recording started"


# Stop recording and translate
def asl_stop_and_translate():

    global recording, recording_file

    print("🛑 Stopping recording...")

    sd.stop()

    write(recording_file.name, fs, recording)

    return asl_translate_audio(recording_file.name)


def asl_translate_audio(filename):

    recognizer = sr.Recognizer()

    with sr.AudioFile(filename) as source:

        audio = recognizer.record(source)

    try:

        text = recognizer.recognize_google(audio)

        print("📝 Recognized:", text)

        play_text_videos(text)

        return text

    except Exception as e:

        print("Error:", e)

        return ""
