import pywhatkit as kit # pip install pywhatkit
import datetime
from speaking_software import *
from Speech_Recogniser import *

# Function to send whatsapp message
def sendMsg():
	print("Who do you want to message?")
	Speak("Who do you want to message?")

	to = input("Enter a number to message: ")
	to = '+91' + to

	print("Message: ", end = "")
	Speak("What is your message?")

	msg = cmd()

	hour = int(datetime.datetime.now().hour)
	minute = int(datetime.datetime.now().minute)
	minute = minute + 1

	kit.sendwhatmsg(to, msg, hour, minute)
	exit()
