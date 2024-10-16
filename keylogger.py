# storing the logs in a txt file while appending every keystroke
file = open("logs.txt", "a")
file.write("Hello World\n")
file.close()