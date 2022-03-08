import pyjokes
from speaking_software import *

# Function to tell jokes
def Jokes():
	My_joke = pyjokes.get_joke(language="en", category="all")

	print(My_joke)
	Speak(My_joke)