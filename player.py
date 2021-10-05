from playsound import playsound

import readchar, os, random, copy

data = os.listdir("audio/")
files = copy.copy(data)

while True:
    letter = readchar.readkey()

    if len(files) <= 1:
        files = copy.copy(data)

    choice = random.choice(files)
    files.remove(choice)

    print(choice.replace(".mp3", ""))

    playsound("audio/"+choice)