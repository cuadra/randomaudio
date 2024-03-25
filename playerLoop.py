import pygame
pygame.mixer.init()
pygame.mixer.music.load("test/file.mp3")
pygame.mixer.music.set_volume(.4)

while True:
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy() == True: pass
