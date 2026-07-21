import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import texttoasl
import speechtoasl
import texttoisl
import speechtoisl

app = Flask(__name__)

# Paths for ASL and ISL dataset
ASL_DATASET = os.path.join(os.path.dirname(__file__), 'dataset', 'asl')
ISL_DATASET = os.path.join(os.path.dirname(__file__), 'dataset', 'isl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/creator')
def creator():
    return render_template('creator.html')

@app.route('/asl')
def asl_home():
    return render_template('asl.html')

@app.route('/isl')
def isl_home():
    return render_template('isl.html')

@app.route('/asl_text')
def asl_text_page():
    return render_template('asl_text.html')

@app.route('/asl_speech')
def asl_speech_page():
    return render_template('asl_speech.html')

@app.route('/isl_text')
def isl_text_page():
    return render_template('isl_text.html')

@app.route('/isl_speech')
def isl_speech_page():
    return render_template('isl_speech.html')

# Serving sign language video datasets
@app.route('/asl_dataset/<path:filename>')
def serve_asl_dataset(filename):
    return send_from_directory(ASL_DATASET, filename)

@app.route('/isl_dataset/<path:filename>')
def serve_isl_dataset(filename):
    return send_from_directory(ISL_DATASET, filename)

# ASL Translation Engine Routes
@app.route("/Atranslate", methods=["POST"])
def asl_translate_text_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    speed = float(data.get("speed", 1.0))
    if text:
        videos = texttoasl.translate_text_to_asl(text)
        return jsonify({"status": "Translation complete!", "videos": videos})
    return jsonify({"status": "Translation failed. Please enter valid text."}), 400

@app.route("/asl_start_recording", methods=["POST"])
def asl_start_recording_route():
    return jsonify({"status": "Recording started..."})

@app.route("/asl_stop_recording", methods=["POST"])
def asl_stop_recording_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if text:
        videos = texttoasl.translate_text_to_asl(text)
        return jsonify({"status": "Translation complete!", "text": text, "videos": videos})
    return jsonify({"status": "Translation failed."}), 400

# ISL Translation Engine Routes
@app.route("/Itranslate", methods=["POST"])
def isl_translate_text_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    speed = float(data.get("speed", 1.0))
    if text:
        videos = texttoisl.translate_text_to_isl(text)
        return jsonify({"status": "Translation complete!", "videos": videos})
    return jsonify({"status": "Translation failed. Please enter valid text."}), 400

@app.route("/isl_start_recording", methods=["POST"])
def isl_start_recording_route():
    return jsonify({"status": "Recording started..."})

@app.route("/isl_stop_recording", methods=["POST"])
def isl_stop_recording_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if text:
        videos = texttoisl.translate_text_to_isl(text)
        return jsonify({"status": "Translation complete!", "text": text, "videos": videos})
    return jsonify({"status": "Translation failed."}), 400

# Chatbot Ashi response logic (Emotionally Intelligent AI Assistant)
@app.route('/chatbot_respond', methods=['POST'])
def chatbot_respond():
    data = request.get_json() or {}
    message = data.get('message', '').strip().lower()
    raw_message = data.get('message', '').strip()
    lang = data.get('lang', 'en')
    profile = data.get('profile', {})
    name = profile.get('name', 'Friend').strip()
    age = profile.get('age', '').strip()
    country = profile.get('country', '').strip()

    # Attempt Gemini API if GEMINI_API_KEY is available in environment
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            system_instruction = (
                f"You are Ashi, the official AI assistant for VYAKT (a sign language translation web platform built by Pratyaksha). "
                f"Your personality is warm, empathetic, highly encouraging, helpful, and emotionally intelligent (like Gemini). "
                f"User Profile: Name = {name}, Age = {age}, Country = {country}, Preferred Language Code = {lang}. "
                f"Always address {name} warmly. Respond in the language matching language code '{lang}'. "
                f"Knowledge about VYAKT:\n"
                f"- Purpose: Facilitates real-time visual sign language translation (Text -> Sign and Speech -> Sign) for Deaf and Hard-of-Hearing accessibility.\n"
                f"- Creator: Created & envisioned by Pratyaksha.\n"
                f"- ASL (American Sign Language): North American one-handed manual alphabet system (1817). Available at /asl, /asl_text, /asl_speech.\n"
                f"- ISL (Indian Sign Language): Standardized by ISLRTC in India, uses two-handed fingerspelling. Available at /isl, /isl_text, /isl_speech.\n"
                f"- Speed Controls: Sliders range from 0.25x (slower pacing for comfortable learning) to 2.00x (faster pacing).\n"
                f"- Speech Recognition: Browser-native local speech recognition for total privacy.\n"
                f"Be empathetic if the user expresses feelings or confusion, and provide helpful guidance."
            )
            model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_instruction)
            response = model.generate_content(raw_message)
            if response and response.text:
                return jsonify({"reply": response.text.strip()})
        except Exception as e:
            print("Gemini API call exception, using intelligent fallback engine:", e)

    # High-Intelligence Empathetic Fallback Engine
import os
from flask import Flask, render_template, request, jsonify, send_from_directory
import texttoasl
import speechtoasl
import texttoisl
import speechtoisl

app = Flask(__name__)

# Paths for ASL and ISL dataset
ASL_DATASET = os.path.join(os.path.dirname(__file__), 'dataset', 'asl')
ISL_DATASET = os.path.join(os.path.dirname(__file__), 'dataset', 'isl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/creator')
def creator():
    return render_template('creator.html')

@app.route('/asl')
def asl_home():
    return render_template('asl.html')

@app.route('/isl')
def isl_home():
    return render_template('isl.html')

@app.route('/learn')
def learn_page():
    return render_template('learn.html')

@app.route('/asl_text')
def asl_text_page():
    return render_template('asl_text.html')

@app.route('/asl_speech')
def asl_speech_page():
    return render_template('asl_speech.html')

@app.route('/isl_text')
def isl_text_page():
    return render_template('isl_text.html')

@app.route('/isl_speech')
def isl_speech_page():
    return render_template('isl_speech.html')

# Serving sign language video datasets
@app.route('/asl_dataset/<path:filename>')
def serve_asl_dataset(filename):
    return send_from_directory(ASL_DATASET, filename)

@app.route('/isl_dataset/<path:filename>')
def serve_isl_dataset(filename):
    return send_from_directory(ISL_DATASET, filename)

# ASL Translation Engine Routes
@app.route("/Atranslate", methods=["POST"])
def asl_translate_text_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    speed = float(data.get("speed", 1.0))
    if text:
        videos = texttoasl.translate_text_to_asl(text)
        return jsonify({"status": "Translation complete!", "videos": videos})
    return jsonify({"status": "Translation failed. Please enter valid text."}), 400

@app.route("/asl_start_recording", methods=["POST"])
def asl_start_recording_route():
    return jsonify({"status": "Recording started..."})

@app.route("/asl_stop_recording", methods=["POST"])
def asl_stop_recording_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if text:
        videos = texttoasl.translate_text_to_asl(text)
        return jsonify({"status": "Translation complete!", "text": text, "videos": videos})
    return jsonify({"status": "Translation failed."}), 400

# ISL Translation Engine Routes
@app.route("/Itranslate", methods=["POST"])
def isl_translate_text_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    speed = float(data.get("speed", 1.0))
    if text:
        videos = texttoisl.translate_text_to_isl(text)
        return jsonify({"status": "Translation complete!", "videos": videos})
    return jsonify({"status": "Translation failed. Please enter valid text."}), 400

@app.route("/isl_start_recording", methods=["POST"])
def isl_start_recording_route():
    return jsonify({"status": "Recording started..."})

@app.route("/isl_stop_recording", methods=["POST"])
def isl_stop_recording_route():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if text:
        videos = texttoisl.translate_text_to_isl(text)
        return jsonify({"status": "Translation complete!", "text": text, "videos": videos})
    return jsonify({"status": "Translation failed."}), 400

# Chatbot Ashi response logic (Emotionally Intelligent AI Assistant)
@app.route('/chatbot_respond', methods=['POST'])
def chatbot_respond():
    data = request.get_json() or {}
    message = data.get('message', '').strip().lower()
    raw_message = data.get('message', '').strip()
    lang = data.get('lang', 'en')
    profile = data.get('profile', {})
    name = profile.get('name', 'Friend').strip()
    age = profile.get('age', '').strip()
    country = profile.get('country', '').strip()

    # Attempt Gemini API if GEMINI_API_KEY is available in environment
    gemini_key = os.environ.get("GEMINI_API_KEY")
    if gemini_key:
        try:
            import google.generativeai as genai
            genai.configure(api_key=gemini_key)
            system_instruction = (
                f"You are Ashi, the official AI assistant for VYAKT (a sign language translation web platform built by Pratyaksha). "
                f"Your personality is warm, empathetic, highly encouraging, helpful, and emotionally intelligent (like Gemini). "
                f"User Profile: Name = {name}, Age = {age}, Country = {country}, Preferred Language Code = {lang}. "
                f"Always address {name} warmly. Respond in the language matching language code '{lang}'. "
                f"Knowledge about VYAKT:\n"
                f"- Purpose: Facilitates real-time visual sign language translation (Text -> Sign and Speech -> Sign) for Deaf and Hard-of-Hearing accessibility.\n"
                f"- Creator: Created & envisioned by Pratyaksha.\n"
                f"- ASL (American Sign Language): North American one-handed manual alphabet system (1817). Available at /asl, /asl_text, /asl_speech.\n"
                f"- ISL (Indian Sign Language): Standardized by ISLRTC in India, uses two-handed fingerspelling. Available at /isl, /isl_text, /isl_speech.\n"
                f"- Speed Controls: Sliders range from 0.25x (slower pacing for comfortable learning) to 2.00x (faster pacing).\n"
                f"- Speech Recognition: Browser-native local speech recognition for total privacy.\n"
                f"Be empathetic if the user expresses feelings or confusion, and provide helpful guidance."
            )
            model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_instruction)
            response = model.generate_content(raw_message)
            if response and response.text:
                return jsonify({"reply": response.text.strip()})
        except Exception as e:
            print("Gemini API call exception, using intelligent fallback engine:", e)

    # High-Intelligence Empathetic Fallback Engine
    # Sentiment & Emotion Detection
    is_confused_or_sad = any(w in message for w in ["help", "sad", "hard", "difficult", "confused", "stuck", "don't know", "cannot understand", "problem", "issue", "trouble", "slow"])
    is_greeting = any(w in message for w in ["hi", "hello", "hey", "greetings", "नमस्ते", "hola", "bonjour", "hallo", "ciao"])
    is_how_are_you = any(w in message for w in ["how are you", "how r u", "आप कैसे हैं", "como estas", "comment ça va", "wie geht", "come stai"])
    is_thanks = any(w in message for w in ["thank", "thanks", " शुक्रिया", "gracias", "merci", "danke", "grazie"])
    
    # Topic Detection
    is_asl = "asl" in message or "american" in message
    is_isl = "isl" in message or "indian" in message
    is_speed = any(w in message for w in ["speed", "slow", "fast", "pace", "0.25", "slider", " गति"])
    is_speech = any(w in message for w in ["speech", "voice", "mic", "speak", "audio", "बोल"])
    is_text = any(w in message for w in ["text", "type", "write", "लिख"])
    is_creator = any(w in message for w in ["creator", "who made", "who built", "pratyaksha", "owner", "developer", "निर्माता"])
    is_manual = any(w in message for w in ["manual", "guide", "how to use", "how do i use", "steps", "usage", "निर्देश"])

    reply = ""

    # Hindi Responses
    if lang == "hi":
        if is_confused_or_sad:
            reply = f"मैं समझ सकती हूँ, {name}। नई भाषा या तकनीक सीखना कई बार कठिन लग सकता है, लेकिन चिंता न करें—व्यक्त पर हर कदम आसान है! आप `/asl_text` या `/isl_text` पर जाकर गति स्लाइडर को **0.25x** पर सेट कर सकते हैं ताकि हर संकेत धीमे और स्पष्ट रूप से दिखाई दे।"
        elif is_asl:
            reply = f"**अमेरिकन साइन लैंग्वेज (ASL)** के बारे में:\n\nASL उत्तरी अमेरिका में उपयोग की जाने वाली मुख्य सांकेतिक भाषा है जो 1817 से एक-हाथ वाले वर्णमाला संकेतों पर आधारित है। हमारे **/asl** पृष्ठ पर आपको A-Z के सभी लाइव संकेत मिलेंगे!"
        elif is_isl:
            reply = f"**भारतीय सांकेतिक भाषा (ISL)** के बारे में:\n\nISL भारत की आधिकारिक सांकेतिक भाषा है, जिसे ISLRTC द्वारा मानकीकृत किया गया है। यह मुख्य रूप से दो-हाथों वाले संकेतों का उपयोग करती है। देखने के लिए **/isl** पृष्ठ पर जाएँ!"
        elif is_speed:
            reply = f"गति नियंत्रण आसान है, {name}! सभी अनुवादक पृष्ठों पर एक **प्लेबैक स्पीड स्लाइडर** मौजूद है। सीखने के लिए इसे **0.25x (धीमी गति)** पर सेट करें, या **2.00x (तेज गति)** तक बढ़ाएँ।"
        elif is_creator:
            reply = f"व्यक्त (VYAKT) को **प्रत्यक्षा (Pratyaksha)** द्वारा परिकल्पित और निर्मित किया गया है, जिसका उद्देश्य कृत्रिम बुद्धिमत्ता (AI) के माध्यम से सांकेतिक भाषा संवाद को सुगम और समावेशी बनाना है।"
        elif is_greeting or is_how_are_you:
            reply = f"नमस्ते {name}! मैं बहुत अच्छी हूँ, पूछने के लिए धन्यवाद। आज व्यक्त पर मैं आपकी क्या मदद कर सकती हूँ?"
        elif is_thanks:
            reply = f"आपका बहुत-बहुत धन्यवाद, {name}! मुझे आपकी मदद करके हमेशा खुशी होती है। यदि कोई और सवाल हो तो ज़रूर पूछें!"
        else:
            reply = f"धन्यवाद, {name}! व्यक्त (VYAKT) पर आप पाठ (Text) और वाणी (Speech) को तुरंत ASL या ISL सांकेतिक भाषा में बदल सकते हैं। मुझसे ASL, ISL, गति नियंत्रण, या मार्गदर्शन के बारे में कुछ भी पूछें!"

    # Spanish Responses
    elif lang == "es":
        if is_confused_or_sad:
            reply = f"Lo entiendo perfectamente, {name}. Aprender lenguaje de señas puede ser un desafío, ¡pero VYAKT está aquí para apoyarte! Puedes ir a `/asl_text` o `/isl_text` y ajustar la velocidad a **0.25x** para ver cada gesto con calma."
        elif is_asl:
            reply = f"**Lenguaje de Señas Americano (ASL)**:\n\nEl ASL es un idioma visual utilizado en América del Norte basado en señas de una sola mano. ¡Visita nuestra página **/asl** para explorar el abecedario interactivo A-Z!"
        elif is_isl:
            reply = f"**Lenguaje de Señas Indio (ISL)**:\n\nEl ISL es el lenguaje de señas estandarizado en India por el ISLRTC. Utiliza principalmente configuraciones de dos manos. ¡Explora **/isl** para ver todos los signos!"
        elif is_speed:
            reply = f"¡Es muy fácil ajustar la velocidad, {name}! En cada traductor encontrarás un deslizador de velocidad. Ajusta desde **0.25x (más lento)** para aprender hasta **2.00x (más rápido)**."
        elif is_creator:
            reply = f"VYAKT fue diseñado y creado por **Pratyaksha** con la visión de hacer la comunicación accesible para todos mediante IA."
        elif is_greeting or is_how_are_you:
            reply = f"¡Hola {name}! Me siento genial, gracias por preguntar. ¿En qué te puedo colaborar hoy en VYAKT?"
        else:
            reply = f"¡Gracias por escribir, {name}! En VYAKT puedes traducir texto y voz a ASL o ISL al instante. Pregúntame lo que quieras sobre navegación, ASL, ISL o ajustes de velocidad."

    # Default English & International Responses (Warm, Empathetic, Gemini-style)
    else:
        if is_confused_or_sad:
            reply = f"I completely understand how you feel, {name}. Learning or navigating sign language tools can sometimes feel overwhelming, but please know that **VYAKT** is designed specifically to support you with total empathy! ❤️\n\nIf you want to take things step-by-step, head over to `/asl_text` or `/isl_text` and slide the playback speed down to **0.25x**. This slows down the sign videos so you can study every single visual movement comfortably."
        elif is_asl:
            reply = f"**American Sign Language (ASL)** is a visual-gestural language widely used across North America. Co-founded in 1817 by Thomas Hopkins Gallaudet and Laurent Clerc, ASL uses a distinctive **one-handed manual alphabet**.\n\nOn VYAKT, you can visit **/asl** to explore the interactive A-Z sign cards, or use **/asl_text** and **/asl_speech** for real-time sentence translation!"
        elif is_isl:
            reply = f"**Indian Sign Language (ISL)** is the primary visual language of the Deaf community in India, standardized by the Indian Sign Language Research and Training Centre (ISLRTC).\n\nUnlike ASL, ISL uses a **two-handed fingerspelling system** and distinctive hand configurations. Check out **/isl** for the complete A-Z reference tool, or **/isl_text** and **/isl_speech** for direct translations!"
        elif is_speed:
            reply = f"Adjusting sign playback speed is effortless, {name}! Every translator page includes a precision speed slider:\n\n• **0.25x – 0.50x**: Slower pacing, perfect for beginners & learning.\n• **1.00x**: Standard natural pacing.\n• **1.50x – 2.00x**: Accelerated pacing for native signers."
        elif is_speech or is_text:
            reply = f"VYAKT features both **Text-to-Sign** and **Speech-to-Sign** translation portals!\n\n• **Text Translation**: Type any sentence into `/asl_text` or `/isl_text` to render video sign sequences.\n• **Speech Translation**: Use `/asl_speech` or `/isl_speech` to speak into your microphone for instant local translation."
        elif is_creator:
            reply = f"VYAKT was envisioned, designed, and built by **Pratyaksha** with a core mission: to harness artificial intelligence to break down communication barriers and create an inclusive world for the Deaf and Hard-of-Hearing community."
        elif is_manual:
            reply = f"Here is your quick **VYAKT Navigation Guide**, {name}:\n\n1. **Home (`/`)**: Overview and language selection.\n2. **ASL Portal (`/asl`)**: American Sign Language A-Z cards & translation tools.\n3. **ISL Portal (`/isl`)**: Indian Sign Language A-Z cards & translation tools.\n4. **Speed Control**: Adjust sliders from 0.25x to 2.00x.\n5. **Ashi AI**: Always here in the bottom right corner whenever you need assistance!"
        elif is_greeting or is_how_are_you:
            reply = f"Hello {name}! I am feeling wonderful and ready to help you today, thank you for asking!\n\nHow can I assist your journey on VYAKT today? Ask me about ASL, ISL, speed adjustments, or site navigation!"
        elif is_thanks:
            reply = f"You are so very welcome, {name}! It is a true pleasure assisting you. If you ever have more questions or need guidance around VYAKT, I am always right here for you!"
        else:
            reply = f"Thank you for messaging me, {name}! As your VYAKT AI assistant, I am here to ensure you have a seamless, empowering experience.\n\nYou can ask me about:\n• **ASL vs ISL** differences and portals\n• **How to use Text or Speech translation**\n• **Adjusting sign video speeds (0.25x to 2.00x)**\n• **Who created VYAKT**\n\nWhat would you like to explore first?"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
