import speech_recognition as sr
# Incase of pyAudio error try these commands
# pip install pipwin
# pipwin install pyaudio
from speaking_software import *

# Function to take voice input commands
def Command():
    try:
        print("Listening...")

        r = sr.Recognizer()
        with sr.Microphone() as source:

            r.pause_threshold = 1

            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)

            query = r.recognize_google(audio)
            query = query.lower()

            print("Recognising...")
            return query

    except Exception as e:
        print("Can you repeat again!!")
        Speak("Can you repeat again!!")
        Command()
