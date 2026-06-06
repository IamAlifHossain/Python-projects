import pygame
import datetime
import time

def set_alarm(alarm_time):
    soundtrack = "Your sound track"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time : {current_time}")
        if current_time==alarm_time:
            print("Wake Up! 😴")
            
            pygame.mixer.init()
            pygame.mixer.music.load(soundtrack)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running = False
        time.sleep(1)


def main():
    alarm_time = input("Set alarm time (HH:MM:SS) : ")
    set_alarm(alarm_time)

if __name__=="__main__":
    main()