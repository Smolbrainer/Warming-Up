import time
import pygame

isTime = False

print(f"The current time is {time.strftime("%H:%M:%S", time.localtime())}.")
alarmTime = str(input("What time do you want to set the alarm to? Write it in this format. Hours:Minutes:Seconds: "))

pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\monfa\Documents\GitHub\Warming-Up\Beginner_Python\Sound\Recording.wav')


while isTime==False:
    currentTime = time.strftime("%H:%M:%S", time.localtime())
    print(f"\rCurrent Time: {currentTime}", end='') # end ='', instructs Python not to add a newline after printing the content. 
    if alarmTime == currentTime:
        print(f"\nIts {currentTime}")
        pygame.mixer.music.play()
        time.sleep(30)
        isTime = True