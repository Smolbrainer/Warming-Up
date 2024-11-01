import random

def getPlayerChoise():
    playerChoice = int(input("Chose one: 1 for Rock, 2 for Paper, and 3 for Scissiors: "))
    if playerChoice> 3 or 1> playerChoice:
        print("Please select 1, 2, or 3.")
        getPlayerChoise()
    else:
        return playerChoice

def startGame():
    numberOfRounds = int(input("How many round do you want to play? "))
    playerScore = 0
    computerScore = 0
    roundNumber = 1

    while numberOfRounds>=roundNumber:
        print(f"This is round number {roundNumber}.")
        input()
        playerChoice = getPlayerChoise()
        computerChoice = random.randrange(1,3)

        if playerChoice == 1 and computerChoice == 1:
            print("Computer chose rock, You chose rock. Draw")
        elif playerChoice == 1 and computerChoice == 2:
            print("Computer chose paper, You chose rock. Paper beats rock. Computer wins the round.")
            computerScore +=1
        elif playerChoice == 1 and computerChoice == 3:
            print("Computer chose scissors, You chose rock. Rock beats scissors. You win the round.")
            playerScore +=1
        elif playerChoice == 2 and computerChoice == 1:
            print("Computer chose rock, you chose paper. Paper beats rock. You win the roung")
            playerScore +=1
        elif playerChoice == 2 and computerChoice == 2:
            print("Computer Chose paper, You chose Paper. Draw")
        elif playerChoice == 2 and computerChoice == 3:
            print("Computer chose Scissors, You Chose paper. Scissocrs beats paper. Computer wins the round.")
            computerScore +=1
        elif playerChoice == 3 and computerChoice == 1:
            print("You chose scissors, Computer chose rock. Rock beats scissors. Computer wins the round.")
            computerScore +=1
        elif playerChoice == 3 and computerChoice == 2:
            print("You chose scissors, Computer chose paper. Scissors beats paper. You win the round.")
            playerScore +=1
        else:
            print("You chose scissors, Computer chose scissors. Draw.")
        roundNumber +=1
        print(f"Score is Computer: {computerScore}, Player: {playerScore}.")
        input()
    endgame(playerScore, computerScore)

def endgame(playerScore, computerScore):
    if playerScore > computerScore:
        print("The player won. Good job!")
    elif computerScore > playerScore:
        print("The computer won. Better luck next time.")
    else:
        print("It was a draw.")
    print(f"The Score was Player: {playerScore}, Computer: {computerScore}.")

    input("Press Any button to play again")
    startGame()

startGame()
