import os
import cv2
import ctypes

# Paths
asl_dataset_path = "C:\\Users\\PRATYAKSHA SINGH\\OneDrive\\Desktop\\COLLEGE\\PROJECTS\\Text-Speech-to-ASL-ISL\\dataset\\asl"
black_video_path = "static/blank.mp4"

window_name = "ASL Translator"


def get_screen_size():

    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()

    return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


def text_to_Asign(text):

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


if __name__ == "__main__":

    user_input = input("Enter text: ")

    text_to_Asign(user_input)
