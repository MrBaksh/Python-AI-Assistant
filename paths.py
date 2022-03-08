import os
import webbrowser
from speaking_software import *

# Function to open Applications and websites
def openApp(query):
	appPath = {
    "chrome" : "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",

    "file explorer" : "C:\\Users\\BAksh\\Desktop\\This PC",

    "vlc player" : "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe",

    "sublime" : "C:\\Program Files\\Sublime Text 3\\sublime_text.exe",

    "ms word" : "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",

    "excel" : "C:\\Program Files\\Microsoft Office\root\\Office16\\EXCEL.EXE",

    "power point" : "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",

    "edge" : "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe",

    "computer management" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\Computer Management.lnk",

    "optimizer" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\dfrgui.lnk",

    "dick clean up" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\Disk Cleanup.lnk",

    "servives" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\services.lnk",

    "system information" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\System Information.lnk",

    "windows defender" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Administrative Tools\\Windows Defender Firewall with Advanced Security.lnk",

    "task manager" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Task Manager.lnk",

    "power shell" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Windows PowerShell\\Windows PowerShell ISE.lnk",

    "remote desktop" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Remote Desktop Connection.lnk",

    "steps recorder" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk",

    "wordpad" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Steps Recorder.lnk",

    "charmap" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\System Tools\\Character Map.lnk",

    "workbench" : "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\MySQL\\MySQL Workbench 8.0 CE.lnk",

    "control panel" : "C:\\Users\\BAksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk",

    "run command" : "C:\\Users\\BAksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run.lnk",

    "command prompt" : "C:\\Users\\BAksh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Run.lnk",

    "facebook" : "facebook.com",

    "instagram" : "instagram.com",

    "twiter" : "twitter.com",

    "youtube" : "youtube.com"
	}
	
	try:
		query = query.replace("open", "")
		os.startfile(appPath[query])
		Speak("Opening" + query)
	except:
		query = query.replace("open", "")
		webbrowser.open("https://" + appPath[query])
		Speak("Opening" + query)
