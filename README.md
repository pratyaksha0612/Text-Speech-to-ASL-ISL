# 🤟 VYAKT: AI-Powered Sign Language Translation & Learning Ecosystem

[![Live Demo](https://img.shields.io/badge/Live_Demo-vyakt.onrender.com-00d2ff?style=for-the-badge&logo=render)](https://vyakt.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**VYAKT** is an intelligent, real-time visual sign language translation and interactive learning ecosystem designed to bridge communication gaps for the Deaf and Hard-of-Hearing community. Envisioned, engineered, and built by **Pratyaksha Singh**, VYAKT transforms spoken and written language into expressive visual sign language sequences across both **American Sign Language (ASL)** and **Indian Sign Language (ISL)**.

---

## 🌟 Live Demo & Deployment

🌐 **Live Web Application**: [https://vyakt.onrender.com](https://vyakt.onrender.com)

---

## ✨ Key Features & Capabilities

### 1. 🤟 Dual Sign Translation Portals (ASL & ISL)
* **Text → Sign Engine**: Parses typed input sentences and dynamically strings together corresponding high-definition sign language video sequences.
* **Speech → Sign Engine**: Integrates browser-native Speech Recognition APIs for 100% private, real-time local voice-to-sign translation.
* **Playback Speed Controls**: Adjust frame rates dynamically from `0.25x` (slower pacing for learning) up to `2.00x` (faster pacing for native signers).

### 2. 🎓 Dedicated Learn Hub (`/learn`)
* **Interactive Alphabet Grid**: Step-by-step studying module for all 26 letters (`A`–`Z`) across both ASL and ISL.
* **Hand Placement Guides**: Detailed hand gesture formation instructions displayed alongside animated sign video demonstrations.

### 3. 🎮 Jumbled Practice Quiz (`/quiz`)
* **Randomized ASL & ISL Questions**: Tests sign recognition skills with jumbled questions.
* **Interactive Wrong Answer Teaching**: Selecting an incorrect choice reveals a step-by-step hand placement guide for that sign, with **`🔄 Try Again`** (re-ask until correct) and **`⏩ Pass / Skip`** options.

### 4. 🖼️ Expandable Reference Video Gallery
* **Fullscreen Modal Viewer**: Clicking any sign card on `/asl` or `/isl` opens an expanded gallery viewer.
* **Carousel & Step Controls**: Features left/right navigation arrows (`‹` and `›`) and a 26-letter interactive thumbnail carousel bar.

### 5. 🤖 Ashi AI Assistant (Emotional Intelligence)
* **Multi-Lingual Companion**: Named after Pratyaksha's real-life nickname (*Ashi*), Ashi provides friendly, multi-lingual support in 6 languages (English, Hindi, Spanish, French, German, Italian).
* **Smart Validation**: Strictly validates onboarding inputs (no gibberish or keyboard mashing) and remembers user profiles.

### 6. 📱 100% Fully Responsive Layout
* Seamless user experience tailored for **Desktops, Laptops (1366px/1440px), Tablets (768px/1024px), and Mobile Devices (320px–480px)**.

---

## 🛠️ Technology Stack & Architecture

* **Backend**: Python 3.10+, Flask, Gunicorn
* **Frontend**: HTML5, Vanilla CSS3 (Custom Glassmorphic System, Google Fonts *Outfit* & *Plus Jakarta Sans*), ES6+ JavaScript
* **Database & Datasets**: H.264 CRF 28 compressed ASL & ISL video datasets
* **APIs**: Web Speech API for local audio processing, optional Gemini AI API integration

---

## 🚀 Local Installation & Setup

### Prerequisites
- Python 3.8+ installed on your system.

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/pratyaksha0612/Text-Speech-to-ASL-ISL.git
   cd Text-Speech-to-ASL-ISL
   ```

2. **Install dependencies**:
   ```bash
   pip install flask gunicorn
   ```

3. **Launch the application**:
   ```bash
   python app.py
   ```

4. **Access in browser**:
   Navigate to `http://127.0.0.1:5000`

---

## 👤 Creator & Author

**Pratyaksha Singh** (Nickname: *Ashi*)  
*Computer Science Student & Accessibility Tech Enthusiast*  
- **LinkedIn**: [pratyaksha-singh-764916277](https://www.linkedin.com/in/pratyaksha-singh-764916277)  
- **GitHub**: [@pratyaksha0612](https://github.com/pratyaksha0612)  
- **Email**: ipratyaksha.works@gmail.com  

---

## 📄 License

This project is open-source and licensed under the **MIT License**.
