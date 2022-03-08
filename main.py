import os
import datetime
import pywhatkit as kit # pip install pywhatkit
import speedtest # pip install speedtest-cli
from wish import *
from RandFacts import *
from decorator import *
from Speech_Recogniser import *
from paths import *
from playSongFunc import *
from pyJokes import *
from speaking_software import *
from speedTest import *
from whatsApp import *
from wikiSearch import *

decorate() # Calling the function to decorate the terminal

Wish() # Calling the function for greeting

while True:
    cmd = Command() # Calling the function to take voice input as command

    
    if 'play' in cmd:
        cmd = cmd.replace("play", " ")
        try:
            kit.playonyt(cmd)
            Speak("Playing" + cmd)
        except:
            Speak("Error in playing ", cmd)
    
    elif 'play song' in cmd:
        playSongs() # Calling the function to play songs

    elif 'open' in cmd:
        openApp(cmd) #Calling the function to open applications
    
    elif 'tell me the time' in cmd:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        Speak(f"Sir, the time is {strTime}")

    elif 'shutdown the machine' in cmd:
        Speak("Shutting down your machine.")
        os.system("shutdown /s")
        
        os.system("shutdown /a")
        Speak("Shut down cancelled.")

    elif 'restart the machine' in cmd:
        Speak("Restart scheduled.")
        os.system("shutdown /r")

    elif 'log out' in cmd:
        Speak("Logging off your account.")
        os.system("shutdown /l")

    elif 'tell some facts' in cmd:
        tellFacts() #Calling the random facts function

    elif 'tell some jokes' in cmd:
        Jokes() #Calling the joke function

    elif 'wikipedia' in cmd:
        searchOnWiki(cmd)

    elif 'download speed' in cmd:
        downSpeed()

    elif 'upload speed' in cmd:
        upSpeed()

    elif 'what is your name' in cmd:
        Speak("My name is Jarvis")

    elif 'what is' in cmd:
        cmd = cmd.replace("what is", "")
        searchOnWiki(cmd) #Making a wikipedia search

    elif 'siri' or 'alexa' or 'cortana' or 'edith' or 'google' in query:
        Speak("I think you are searching someone else. I  am Jarvis")

    elif 'who built you' in cmd:
        Speak("Sikandar Baksh made me with Python programing")


    elif 'sleep' in cmd:
        Speak("Well, closing the program")
        exit()

    elif 'exit' in cmd:
        Speak("Well, closing the program")
        exit()