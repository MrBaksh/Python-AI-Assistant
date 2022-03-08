import pyttsx3 # pip install pyttsx3

# Function for voice output
def Speak(command):
    bot = pyttsx3.init()
    # In order to get a female voice output uncomment the below two lines
    #voice_id = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    #engine.setProperty('voice', voice_id)
    bot.setProperty("rate", 150)
    bot.say(command)
    bot.runAndWait()
