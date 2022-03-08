import datetime
from speaking_software import *

# Function to give a greeting wish
def Wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        Speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        Speak("Good Afternoon!")

    else:
        Speak("Good Evening!")

    Speak("I am your Assistant, how can I help you??")
    