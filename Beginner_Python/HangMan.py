import requests
import random

#word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
#response = requests.get(word_site)
WORDS = open(r'C:\Users\monfa\Desktop\We code\Beginner\words.txt').read().split() # The r before the string indicated its a raw string. Backslashes typically used as escape characters (eg. \n becomes new line)
#.split() splits a string into a list of substrings based on a specified delimeter (Which is space by default)
#WORDS = response.text.splitlines() # .text makes it so we get the words as strings not bytes. ### .content.decode('utf-8').splitlines could be used instead which splits the lines in the list and decodes them from bytes to strings


def startGame():   
    global chosenWord 
    chosenWord = list(random.choice(WORDS))
    global answer 
    answer = ["_"] * (len(chosenWord))
    global numberOfGuesses 
    numberOfGuesses = int(input(f"The word is {len(chosenWord)} letters, How many incorrect guesses do you want? ")) #len() gets the number of objects in a container.
    if numberOfGuesses<=0:
        print("You are so silly you cant do that the number has to be bigger than 0!")
        startGame()
    global guessesWrong 
    guessesWrong = 0
    global lettersGuessed 
    lettersGuessed = []

    getGuess(guessesWrong)


def checkGuess(guess,guessesWrong):
    correct = 0
    oldAnswer = list(answer)

    for i in range(len(chosenWord)):
        if chosenWord[i] == guess:
            answer[i] = guess
            correct += 1
            if answer == chosenWord:
                wonGameOver(answer)

    if oldAnswer == answer:
        guessesWrong +=1
        print(f"Nope that is incorrect. You have {numberOfGuesses - guessesWrong} guesses remaining")
        
    print(f"You got {correct} correct. {answer}")
    guessesWrong = getGuess(guessesWrong)
    return answer
        
def getGuess(guessesWrong):
    if numberOfGuesses>guessesWrong:
        guess = str(input(f"You've Guesseed {lettersGuessed} so far. Guess a letter! Make sure its 1 singular letter: "))

        for i in range(len(lettersGuessed)):
            if guess == lettersGuessed[i]:
                print("You already guessed that letter ser no can do")
                getGuess(guessesWrong)
        lettersGuessed.append(guess)
        checkGuess(guess,guessesWrong)
    else:
        gameOver()

def wonGameOver(answer):
    answerString = ''.join(answer) # ''.join() joins the list together and fills the space between the stuff in the list with '' whatever u put inside
    print(answer)
    print(f"You won gang the word was {answerString}.")
    input("Press enter if you would like to play again")
    startGame()

def gameOver():
    print(f"Looks like you are out of guesses. The word was {''.join(chosenWord)}. Press enter if you would like to to play again:")
    input()
    startGame()



startGame()


