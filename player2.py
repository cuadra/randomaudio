from pygame import mixer

import readchar, os, random, copy

data = os.listdir("audio/")
files = copy.copy(data)

mixer.init()

while True:
    letter = readchar.readkey()

    if len(files) <= 1:
        files = copy.copy(data)

    choice = random.choice(files)
    files.remove(choice)

    print(choice.replace(".mp3", ""))

    mixer.music.load("audio/"+choice)
    mixer.music.set_volume(1)
    mixer.music.play()