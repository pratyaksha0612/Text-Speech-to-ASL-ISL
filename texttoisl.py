import os
import cv2

# Paths
isl_dataset_path = "C:/Users/Chhavi/Desktop/text-speech-to-sign/dataset/isl"
black_video_path = "static/blank.mp4"  # Shown for space

# Resize ratio for letter videos
resize_ratio = 0.5

def display_video(video_path, resize=True):
    if not os.path.exists(video_path):
        print(f"❌ Video not found at: {video_path}")
        return False

    cap = cv2.VideoCapture(video_path)

    # Create one consistent window
    window_name = "Sign Language Translator"
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
    cv2.destroyAllWindows()
    return True

def text_to_Isign(text):
    for char in text:
        if char.isalpha():
            video_path = os.path.join(isl_dataset_path, f"{char.lower()}.mp4")
            if not display_video(video_path, resize=True):
                break
        elif char == " ":
            if not display_video(black_video_path, resize=False):
                break

    cv2.destroyAllWindows()

# Only runs interactively if called from terminal
if __name__ == "__main__":
    user_input = input("Please enter the text: ")
    text_to_IIsign(user_input)
