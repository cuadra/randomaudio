import pygame
pygame.mixer.init()
pygame.mixer.music.load("audio/ambience.mp3")
pygame.mixer.music.set_volume(.2)

while True:
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy() == True: pass