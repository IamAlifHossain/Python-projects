import time
import pygame
soundtrack = "Your sound track"
duration = int(input("Input timer duration = "))

for x in range(duration,0,-1):
    sec = x%60
    min = int((x/60)%60)
    hour = int(x/3600)
    print(f"{hour:02}:{min:02}:{sec:02}")
    time.sleep(1)

print("Time's up!")
pygame.mixer.init()
pygame.mixer.music.load(soundtrack)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)