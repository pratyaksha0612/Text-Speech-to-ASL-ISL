from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Paths
isl_dataset_path = "C:/Users/Chhavi/Desktop/text-speech-to-sign/dataset/isl"
black_video_path = "static/blank.mp4"  # Shown for space

# Resize ratio for letter videos
resize_ratio = 0.5

def get_video_path(char):
    if char.isalpha():
        return os.path.join(isl_dataset_path, f"{char.lower()}.mp4")
    elif char == " ":
        return black_video_path
    return None

@app.route('/')
def index():
    return render_template('isl_text.html')

@app.route('/get_videos', methods=['POST'])
def get_videos():
    text = request.json['text']
    videos = []
    
    for char in text:
        video_path = get_video_path(char)
        if video_path and os.path.exists(video_path):
            videos.append(video_path)
        else:
            videos.append(None)

    return jsonify(videos)

if __name__ == '__main__':
    app.run(debug=True)
