import speedtest # pip install speedtest-cli
from speaking_software import *

st = speedtest.Speedtest()

# Function to check download speed
def downSpeed():
	print("Calculating...")
	speed = st.download()/1024/1024
	speed = round(speed, 2)
	print(str(speed) + " Mbps")
	Speak("Current download speed is {} MBPS".format(speed))

# Function to check upload speed
def upSpeed():
	print("Calculating...")
	speed = st.upload()/1024/1024
	speed = round(speed, 2)
	print(str(speed) + " Mbps")
	Speak("Current upload speed is {} MBPS".format(speed))

	