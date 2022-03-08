import pyfiglet # pip install pyfiglet==0.7
import os

# Function to decorate command prompt
def decorate():
	os.system("cls")
	result = pyfiglet.figlet_format("Welcome to Python AI Assistant")
	print("****************************************************************************************************************************************************")
	print(result)
	print("****************************************************************************************************************************************************")
