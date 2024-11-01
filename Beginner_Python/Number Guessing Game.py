import random

print(f"The objective of this game is to correctly guess a number that is randomly generated. Please Specify the lowest number and largest number that you want to be generated: ")
firstRange = int(input("What the lowest number? "))
secondRange = int(input("What is the largest number? "))
numberOfGuesses = int(input("How many guesses do you want? "))
computerGuess = int(random.randrange(firstRange,secondRange))
numberofGuessed = 1

def getUserGuess (numberofGuessed):
    userGuess = int(input(f"You are on Guess Number {numberofGuessed},  Guess a number! "))

    if userGuess>secondRange or userGuess<firstRange:
        print(f"Please chose a number between your specified range which was {firstRange},{secondRange} thank you")
        return getUserGuess(numberofGuessed)
    else:
        return userGuess

def checkGuess (numberofGuessed):
    while numberOfGuesses>=numberofGuessed:
        userGuess = getUserGuess(numberofGuessed)
        
        if computerGuess == userGuess:
            print(f"Congrats you guessed correctly the number was {computerGuess}") 
            return
        elif userGuess > computerGuess:
            print(f"Too high try again")
        else:
            print(f"Too low gang try again")
            
        numberofGuessed +=1
    print(f"You out of guesses the correct number was {computerGuess}.")
    


checkGuess(numberofGuessed)

