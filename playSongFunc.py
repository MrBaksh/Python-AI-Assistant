import random
import os
from speaking_software import *

# Function to play songs from directory
def playSongs():
    path = "E:\\Videos\\Songs"
    music_dir = os.listdir(path)

    length = len(music_dir)

    if length > 0:
        i = random.randint(1, length)
        try:
            pathOfFile = path + "\\" + music_dir[i]
            Speak("Okay, playing song for you.")
            os.startfile(pathOfFile)
        except Exception as e:
            print(e)
    else:
        Speak("No song in the directory!")
