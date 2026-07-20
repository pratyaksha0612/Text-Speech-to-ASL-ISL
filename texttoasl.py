import os

# Base Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASL_DATASET = os.path.join(BASE_DIR, 'dataset', 'asl')
BLANK_VIDEO = "/static/blank.mp4"

def translate_text_to_asl(text):
    """
    Translates text into a list of web-accessible ASL video paths.
    """
    videos = []
    if not text:
        return videos
    for char in text.lower():
        if char.isalpha():
            filename = f"{char}.mp4"
            filepath = os.path.join(ASL_DATASET, filename)
            if os.path.exists(filepath):
                videos.append(f"/asl_dataset/{filename}")
        elif char == " ":
            videos.append(BLANK_VIDEO)
    return videos

if __name__ == "__main__":
    user_input = input("Enter text: ")
    res = translate_text_to_asl(user_input)
    print("ASL Video Queue:", res)


