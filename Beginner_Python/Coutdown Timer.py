#Create a countdown timer that takes user input for the time and counts down to zero, displaying the time remaining.

from datetime import datetime, timedelta
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\monfa\Documents\GitHub\Warming-Up\Beginner_Python\Sound\Recording.wav')

def start():
    x = int(input("Do you want a countdown or a timer? 1 for countdown 2 for timer. "))
    if x == 1: 
        countdown()
    if x == 2:
        timer()
    else:
        print("Make sure to put 1 or 2 next time")
        start()

def countdown():
    countdown = abs(int(input("What number r u counting down from in second? "))) #Abs() is absolute value to make sure its positive
    for i in range((countdown)+1):
        print(f"\r{countdown}       ", end='') #the extra spaces makes sure to replace the 0 cause going from 10 to 9 makes it 90 since \r just overwrites
        countdown -=1
        time.sleep(1)
    pygame.mixer.music.play()
    time.sleep(30)

    input("\nPress enter to play again")
    start()

def timer():
    x = int(input("Are you using a 24 hour format or 12 hour format. 1 for 24; 2 for 12: "))
    if x == 1:
        timer = datetime.strptime(input("What time do you want to set the alarm to? Write it in this format. (Hours:Minutes:Seconds): "),'%H:%M:%S').time().replace(microsecond=0)
    elif x == 2:
        PMorAM = int(input("Is it AM or PM? 1 for AM 2 for PM: "))
        if PMorAM == 1:
            timer = datetime.strptime(input("What time do you want to set the alarm to? Write it in this format. (Hours:Minutes:Seconds): "),'%H:%M:%S').time().replace(microsecond=0) 
        if PMorAM == 2:
            timer = ((datetime.strptime(input("What time do you want to set the alarm to? Write it in this format. (Hours:Minutes:Seconds): "),'%H:%M:%S')) + timedelta(hours = 12)).time().replace(microsecond=0) #adds 12 hours so 4pm becomes 16
        else:
            print("Make sure to put 1 or 2 next time")
            timer()
    else:
        print("Make sure to put 1 or 2 next time")
        timer()
    


    while True:
        currentTime = datetime.now().time().replace(microsecond=0)
        timeRemaining =  datetime.combine(datetime.today(), timer) - datetime.combine(datetime.today(), currentTime)
        print(f'\rCurrent Time: {currentTime}\n\rTime Remaining: {timeRemaining} \033[F', end='') #\r moves the cursor to the beginnening of the current line, without advancing to the next time. It lets you overwrite the current line.
        if currentTime >= timer:
            print("\n\nAlarm time reached!")
            pygame.mixer.music.play()
            time.sleep(30)
            break
        time.sleep(1)

    input("Press enter to play again")
    start()

start()