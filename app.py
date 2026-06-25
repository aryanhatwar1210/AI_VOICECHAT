import streamlit as st
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import os
import google.generativeai as genai


# Page Config
st.set_page_config(
    
    page_title="NOVA AI Assistant",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

.stButton>button {
    width: 100%;
    height: 60px;
    font-size: 22px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 NOVA AI Voice Assistant")
col1, col2 = st.columns([1,2])

with col1:
    st.image("bnova.png", width=1000)

# with col2:
#     st.markdown("## 👋 Hey! I am Nova")
#     st.markdown("### Please say something 🎤")

st.markdown("### Voice Controlled Smart Assistant")


engine = pyttsx3.init()
api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")
def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

apps = {
    "chrome": "start chrome",
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "vs code": "code"
}

if  st.button("🎤 START LISTENING"):
    st.success("🟢 Nova is Listening...")

    with st.spinner("Listening..."):
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            command = recognizer.recognize_google(audio).lower()

            st.markdown("### 🗣 You Said")
            st.info(command)

            if "open youtube" in command:
                webbrowser.open("https://youtube.com")
                st.success("Opening YouTube")

            elif "open google" in command:
                webbrowser.open("https://google.com")
                st.success("Opening Google")

            elif "open whatsapp" in command:
                webbrowser.open("https://web.whatsapp.com")
                st.success("Opening WhatsApp")

            elif "open gmail" in command:
                webbrowser.open("https://mail.google.com")
                st.success("Opening Gmail")

            elif "open linkedin" in command:
                webbrowser.open("https://linkedin.com")
                st.success("Opening LinkedIn")

            elif "open map" in command:
                webbrowser.open("https://maps.google.com")
                st.success("Opening Google Maps")

            elif "open spotify" in command:
                webbrowser.open("https://spotify.com")
                st.success("Opening Spotify")

            elif "time" in command:
                current_time = datetime.now().strftime("%I:%M %p")
                st.info(current_time)

            elif "open" in command:
                app = command.replace("open", "").strip()

                if app in apps:
                    os.system(apps[app])
                    st.success(f"Opening {app}")
                

                else:
                    os.system(f"start {app}")
                    st.success(f"Trying to open {app}")
            else:
                    with st.spinner("AI Thinking..."):
                        response = model.generate_content(command)

                    answer = response.text

                    st.markdown("### 🤖 Nova")
                    st.success(answer)

                    speak(answer)

        except Exception as e:
            st.error(str(e))