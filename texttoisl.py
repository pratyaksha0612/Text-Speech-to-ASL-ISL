import os

# Base Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ISL_DATASET = os.path.join(BASE_DIR, 'dataset', 'isl')
BLANK_VIDEO = "/static/blank.mp4"

def translate_text_to_isl(text):
    """
    Translates text into a list of web-accessible ISL video paths.
    """
    videos = []
    if not text:
        return videos
    for char in text.lower():
        if char.isalpha():
            filename = f"{char}.mp4"
            filepath = os.path.join(ISL_DATASET, filename)
            if os.path.exists(filepath):
                videos.append(f"/isl_dataset/{filename}")
        elif char == " ":
            videos.append(BLANK_VIDEO)
    return videos

if __name__ == "__main__":
    user_input = input("Enter text: ")
    res = translate_text_to_isl(user_input)
    print("ISL Video Queue:", res)


