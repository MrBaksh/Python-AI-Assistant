import randfacts # pip install randfacts
from speaking_software import *

# Function to tell some random facts
def tellFacts():
	facts = randfacts.get_fact()
	print(facts)
	Speak(facts)
