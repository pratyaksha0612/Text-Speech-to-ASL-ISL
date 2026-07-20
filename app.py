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

# Chatbot Ashi response logic (multilingual text assistant)
@app.route("/chatbot_respond", methods=["POST"])
def chatbot_respond():
    data = request.get_json() or {}
    message = data.get("message", "").strip().lower()
    lang = data.get("lang", "en").strip().lower()
    profile = data.get("profile", {})
    
    name = profile.get("name", "User") or "User"
    age = profile.get("age", "")
    country = profile.get("country", "")
    
    accessibility_keywords = ["deaf", "mute", "cannot speak", "cannot hear", "hard of hearing", "speaking problem", "hearing problem", "disabled", "disability", "speech impairment", "struggle", "difficult", "frustrated", "lonely", "sad", "help me", "सुन", "बोल", "दिव्यांग", "मदद"]
    manual_keywords = ["manual", "guide", "how to use", "tutorial", "instructions", "help with site", "features", "website help", "pages", "navigation", "निर्देशिका", "मार्गदर्शन", "मदद", "guia", "aide"]
    asl_keywords = ["asl", "american sign", "एएसएल", "अमेरिकन"]
    isl_keywords = ["isl", "indian sign", "आईएसएल", "भारतीय"]
    speed_keywords = ["speed", "slow", "pace", "fast", "गति", "धीमा", "तेज", "vitesse", "velocidad", "velocità"]
    creator_keywords = ["creator", "who made", "founder", "pratyaksha", "निर्माता", "बनाया", "प्रत्यक्षा"]
    
    responses = {
        "greetings": {
            "en": f"Hello {name}! How can I help you today on VYAKT?",
            "hi": f"नमस्ते {name}! आज व्यक्त पर मैं आपकी क्या सहायता कर सकता हूँ?",
            "es": f"Hola {name}! ¿Cómo te puedo ayudar hoy en VYAKT?",
            "fr": f"Bonjour {name}! Comment puis-je vous aider aujourd'hui sur VYAKT ?",
            "de": f"Hallo {name}! Wie kann ich Ihnen heute auf VYAKT helfen?",
            "it": f"Ciao {name}! Come posso aiutarti oggi su VYAKT?"
        },
        "how_are_you": {
            "en": f"I am feeling wonderful, {name}! Thank you for asking. I hope you are having an amazing and accessible experience on our platform.",
            "hi": f"मैं बहुत अच्छा महसूस कर रहा हूँ, {name}! पूछने के लिए धन्यवाद। आशा है कि आपका अनुभव व्यक्त पर शानदार रहेगा।",
            "es": f"¡Me siento fantástico, {name}! Gracias por preguntar. Espero que tengas una experiencia increíble en nuestra plataforma.",
            "fr": f"Je me sens fantastique, {name} ! Merci de demander. J'espère que vous passez un excellent moment sur notre plateforme.",
            "de": f"Mir geht es hervorragend, {name}! Vielen Dank der Nachfrage. Ich hoffe, Sie haben eine barrierefreie Erfahrung auf unserer Plattform.",
            "it": f"Mi sento benissimo, {name}! Grazie per averlo chiesto. Spero che la tua esperienza sulla nostra piattaforma sia fantastica."
        },
        "empathy": {
            "en": f"Thank you for sharing that, {name}. VYAKT is here to support you with our Text to Sign and Speech to Sign portals. You can type sentences or speak into the microphone to translate, and slow down playback speed to 0.25x for comfortable learning.",
            "hi": f"बताने के लिए धन्यवाद, {name}। व्यक्त आपकी सहायता के लिए तैयार है। आप बोलकर या लिखकर संकेत अनुवाद देख सकते हैं और समझने के लिए गति को 0.25x तक धीमा कर सकते हैं।",
            "es": f"Gracias por compartirlo, {name}. VYAKT está aquí para ayudarte con la traducción de texto o voz, permitiéndote cambiar la velocidad hasta 0.25x para facilitar el aprendizaje.",
            "fr": f"Merci de partager cela, {name}. VYAKT est là pour vous aider avec nos outils de texte et de voix. Vous pouvez ajuster la vitesse jusqu'à 0.25x pour mieux comprendre.",
            "de": f"Danke fürs Teilen, {name}. VYAKT hilft Ihnen mit Text-zu-Gebärde und Sprache-zu-Gebärde Übersetzungsfunktionen, bei denen Sie das Tempo auf 0.25x drosseln können.",
            "it": f"Grazie per aver condiviso, {name}. VYAKT è qui per assisterti con i traduttori di testo e voce. Puoi regolare la velocità dei video fino a 0.25x per facilitare l'apprendimento."
        },
        "manual": {
            "en": "VYAKT User Manual:\n1. Home Page: Introduction and portals.\n2. ASL Portal (/asl): American Sign Language Text and Speech translation.\n3. ISL Portal (/isl): Indian Sign Language Text and Speech translation.\n4. Speed Adjustment: Adjust speeds (0.25x to 2.00x) via sliders.",
            "hi": "व्यक्त निर्देशिका:\n1. मुख्य पृष्ठ: परिचय और मार्ग।\n2. ASL पोर्टल (/asl): अमेरिकन साइन लैंग्वेज अनुवाद।\n3. ISL पोर्टल (/isl): भारतीय सांकेतिक भाषा अनुवाद।\n4. गति नियंत्रण: प्लेबैक गति स्लाइडर (0.25x से 2.00x)।",
            "es": "Manual del Usuario:\n1. Inicio: Guía general y accesos.\n2. Portal ASL: Traductores de texto y voz.\n3. Portal ISL: Traductores de texto y voz indios.\n4. Velocidad: Control de reproducción (0.25x a 2.00x).",
            "fr": "Guide d'utilisation VYAKT :\n1. Accueil : Présentation générale.\n2. Portail ASL : Outils de traduction.\n3. Portail ISL : Traduction et alphabet indiens.\n4. Vitesse : Ajustement de 0.25x à 2.00x.",
            "de": "Benutzerhandbuch:\n1. Home: Hauptmenü.\n2. ASL-Portal: Text- und Sprachübersetzung.\n3. ISL-Portal: Indische Gebärdensprache.\n4. Tempo: Regelbar von 0.25x bis 2.00x.",
            "it": "Guida per l'utente:\n1. Home: Introduzione.\n2. Portale ASL: Traduttore testo e voce.\n3. Portale ISL: Traduttori indiani.\n4. Velocità: Regolabile da 0.25x a 2.00x."
        },
        "asl": {
            "en": "American Sign Language (ASL) is a visual-gestural language used in North America. Visit our /asl page to use the interactive A-Z alphabet reference tool or translate typed sentences.",
            "hi": "अमेरिकन साइन लैंग्वेज (ASL) उत्तरी अमेरिका में प्रयुक्त होने वाली सांकेतिक भाषा है। /asl पर जाकर अक्षर सूची और अनुवादक देखें।",
            "es": "La Lengua de Señas Americana (ASL) es el idioma visual usado en América del Norte. Explora /asl para ver el abecedario e iniciar traducción.",
            "fr": "L'American Sign Language (ASL) est la langue des signes utilisée en Amérique du Nord. Naviguez vers /asl pour voir l'alphabet.",
            "de": "Amerikanische Gebärdensprache (ASL) wird in Nordamerika genutzt. Auf /asl finden Sie das interaktive Alphabet.",
            "it": "La lingua dei segni americana (ASL) è usata in Nord America. Vai su /asl per vedere l'alfabeto completo."
        },
        "isl": {
            "en": "Indian Sign Language (ISL) is the primary sign language in India. Go to the /isl page to view the standardized A-Z signs and access text/speech translators.",
            "hi": "भारतीय सांकेतिक भाषा (ISL) भारत में प्रयुक्त प्राथमिक सांकेतिक भाषा है। /isl पर जाकर अक्षरों के दो-हाथ वाले संकेत और अनुवादक देखें।",
            "es": "La Lengua de Señas India (ISL) es la principal en la India. Visita la página /isl para ver los gestos A-Z.",
            "fr": "L'ISL est la principale langue des signes en Inde. Visitez /isl pour l'alphabet et les traducteurs.",
            "de": "Indische Gebärdensprache (ISL) wird in Indien genutzt. Auf /isl finden Sie das Alphabet.",
            "it": "La lingua dei segni indiana (ISL) è usata in India. Vai su /isl per l'alfabeto e i traduttori."
        },
        "speed": {
            "en": "Speed Adjustments: You can modify the translation speed (0.25x for slower speed, up to 2.00x for native speed) using the speed sliders available on all translator pages.",
            "hi": "गति नियंत्रण: आप संकेतों की गति 0.25x से 2.00x तक बदल सकते हैं। यह स्लाइडर सभी अनुवाद पृष्ठों पर उपलब्ध है।",
            "es": "Ajuste de Velocidad: Puedes cambiar la velocidad de 0.25x a 2.00x usando el deslizador en las páginas de traducción.",
            "fr": "Vitesse : Ajustez le rythme des signes de 0.25x à 2.00x via les curseurs des traducteurs.",
            "de": "Tempo: Passen Sie die Geschwindigkeit der Gebärden-Videos per Schieberegler von 0.25x bis 2.00x an.",
            "it": "Regolazione Velocità: Puoi variare la velocità dei segni da 0.25x a 2.00x tramite gli appositi cursori."
        },
        "creator": {
            "en": "Platform Creator: VYAKT was envisioned and built by Pratyaksha. The mission of this project is to build communication bridges using artificial intelligence.",
            "hi": "मंच के निर्माता: व्यक्त को प्रत्यक्षा द्वारा परिकल्पित और निर्मित किया गया था। इस परियोजना का उद्देश्य एआई का उपयोग करके सुगम संवाद मार्ग बनाना है।",
            "es": "Creador de la Plataforma: VYAKT fue diseñado y creado por Pratyaksha con el propósito de facilitar la comunicación usando inteligencia artificial.",
            "fr": "Créateur : VYAKT a été imaginé et construit par Pratyaksha pour créer des ponts de communication grâce à l'IA.",
            "de": "Schöpfer: VYAKT wurde von Pratyaksha entworfen und entwickelt, um Barrieren mithilfe von KI abzubauen.",
            "it": "Creatore: VYAKT è stato ideato e creato da Pratyaksha per abbattere le barriere comunicative tramite l'IA."
        },
        "default": {
            "en": f"Thank you for messaging me, {name}! I am here to help you get the most out of VYAKT. Ask me to guide you around the site, show details about ASL/ISL, or explain speed adjustments.",
            "hi": f"संपर्क करने के लिए धन्यवाद, {name}! मैं यहाँ आपकी मदद के लिए हूँ। मुझसे साइट पर नेविगेट करने, ASL/ISL, या प्लेबैक गति नियंत्रण के बारे में पूछें।",
            "es": f"¡Gracias por tu mensaje, {name}! Estoy aquí para ayudarte. Pregúntame sobre el manual, ASL, ISL o el control de velocidad.",
            "fr": f"Merci pour votre message, {name} ! Je suis là pour vous assister. Demandez-moi des détails sur la navigation, l'ASL/ISL ou la vitesse.",
            "de": f"Vielen Dank für Ihre Nachricht, {name}! Fragen Sie mich nach dem Handbuch, Details zu ASL/ISL oder zur Geschwindigkeit.",
            "it": f"Grazie per il messaggio, {name}! Sono qui per aiutarti. Chiedimi del manuale, di ASL/ISL o della regolazione velocità."
        }
    }
    
    def get_res(key):
        l = lang if lang in responses[key] else "en"
        return responses[key][l]
        
    if any(kw in message for kw in accessibility_keywords):
        reply = get_res("empathy")
    elif any(kw in message for kw in manual_keywords):
        reply = get_res("manual")
    elif any(kw in message for kw in asl_keywords):
        reply = get_res("asl")
    elif any(kw in message for kw in isl_keywords):
        reply = get_res("isl")
    elif any(kw in message for kw in speed_keywords):
        reply = get_res("speed")
    elif any(kw in message for kw in creator_keywords):
        reply = get_res("creator")
    elif any(x in message for x in ["hello", "hi", "hey", "greetings", "नमस्ते", "hola", "bonjour", "hallo", "ciao"]):
        reply = get_res("greetings")
    elif "how are you" in message or "आप कैसे हैं" in message or "como estas" in message or "comment ça va" in message or "wie geht" in message or "come stai" in message:
        reply = get_res("how_are_you")
    else:
        reply = get_res("default")
        
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
