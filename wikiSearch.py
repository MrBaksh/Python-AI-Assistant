import wikipedia # pip install wikipedia
from speaking_software import *

# Function to search wikipedia articles
def searchOnWiki(query):
    Speak("Searching on wikipedia...")
    try:
        query = query.replace("wikipedia", "")
    except:
        pass
    result = wikipedia.summary(query, sentences=2)
    Speak("According to wikipedia")
    print(result)
    Speak(result)
