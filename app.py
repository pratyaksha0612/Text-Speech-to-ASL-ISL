from flask import Flask, render_template, request, jsonify
from texttoisl import text_to_Isign
from texttoasl import text_to_Asign
from speechtoisl import isl_start_recording, isl_stop_and_translate
from speechtoasl import asl_start_recording, asl_stop_and_translate
import threading

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/asl')
def asl():
    return render_template('asl.html')

@app.route('/isl')
def isl():
    return render_template('isl.html')

@app.route('/isl_text')
def isl_text():
    return render_template('isl_text.html')

@app.route('/isl_speech')
def isl_speech():
    return render_template('isl_speech.html')

def run_isl_video_in_thread(text):
    thread = threading.Thread(target=text_to_Isign, args=(text,))
    thread.start()

@app.route("/Itranslate", methods=["POST"])
def Itranslate():
    data = request.get_json()
    text = data.get("text", "")
    
    if text:
        run_isl_video_in_thread(text)
        return jsonify({"status": "Translation playing live..."})
    
    return jsonify({"error": "No text provided"}), 400

@app.route("/isl_start_recording", methods=["POST"])
def isl_start_recording_route():
    status = isl_start_recording()  # Starts the recording process
    return jsonify({"status": status})

# Stop recording and translate
@app.route("/isl_stop_recording", methods=["POST"])
def isl_stop_recording_route():
    text = isl_stop_and_translate()  # Stops recording and performs translation
    if text:
        return jsonify({"status": "Translation complete!", "text": text})
    return jsonify({"status": "Translation failed."}), 400

# === ASL ROUTES ===
@app.route('/asl_text')
def asl_text():
    return render_template('asl_text.html')

@app.route('/asl_speech')
def asl_speech():
    return render_template('asl_speech.html')

def run_asl_video_in_thread(text):
    thread = threading.Thread(target=text_to_Asign, args=(text,))
    thread.start()

@app.route("/Atranslate", methods=["POST"])
def Atranslate():
    data = request.get_json()
    text = data.get("text", "")
    
    if text:
        run_asl_video_in_thread(text)
        return jsonify({"status": "Translation playing live..."})
    
    return jsonify({"error": "No text provided"}), 400

@app.route("/asl_start_recording", methods=["POST"])
def asl_start_recording_route():
    status = asl_start_recording()  # Starts the recording process
    return jsonify({"status": status})

# Stop recording and translate
@app.route("/asl_stop_recording", methods=["POST"])
def asl_stop_recording_route():
    text = asl_stop_and_translate()  # Stops recording and performs translation
    if text:
        return jsonify({"status": "Translation complete!", "text": text})
    return jsonify({"status": "Translation failed."}), 400


if __name__ == '__main__':
    app.run(debug=True)
