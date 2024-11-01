import numpy

def startGame():
    numberOfDice = int(input("How many dice do you wish to roll? "))

    if numberOfDice<=0:
        print("You are so silly you can't do that")
        startGame()

    smallestNumber = int(input("What do you want the smallest number that the dice can roll to be? "))
    largestNumber = int(input("What do you want the largest number that the dice can roll to be? "))
    totalResult = 0

    diceResults = numpy.random.randint(smallestNumber,largestNumber+1,numberOfDice)

    for i in range(len(diceResults)): #len() returns the number of items in a container
        print(f"Dice {i+1} rolled {diceResults[i]}.")
        totalResult += diceResults[i]

    input()
    print(f"The total of the roll was {totalResult}.")
    print("Press enter to start over again!")
    input()
    startGame()

startGame()

