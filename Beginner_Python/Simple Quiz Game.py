# User has to follow the exact format of the sample quiz game files that were provided.

import re

def getChoices(questionFile):
    choices = []
    choiceList = []
    for lines in questionFile:
        lines = lines.strip()
        if not re.match(r'^\d.*\?$', lines): # checks to see if its not a question
            choices.append(lines)
        else:
            if choices: #checks to make sure choices isnt empty
                choiceList.append(choices)
                choices = []
    if choices:
        choiceList.append(choices)
    return(choiceList)

def startQuiz():
    score = 0
    for i in quiz:
        print(i['Question'])
        for k in i['Choices']:
            print(k)
        answer = str(input("Whats the answer? "))
        if answer.lower() == i['Answer'].lower():
            print(f'{i['Answer']} is Correct!')
            score +=1
        else:
            print(f"Thats incorrect, The correct answer was {i['Answer']}")
        input()

    print(f"Your final grade was {score}/{len(quiz)}")

questionFile = open(r'C:\Users\monfa\Documents\GitHub\Warming-Up\Beginner_Python\Simple Quiz Game Files\Questions.txt').readlines()
questions = [line.strip() for line in questionFile if re.match(r'^\d.*\?$', line.strip())]
answers = open(r'C:\Users\monfa\Documents\GitHub\Warming-Up\Beginner_Python\Simple Quiz Game Files\Answers.txt').read().splitlines()

choices = getChoices(questionFile)

quiz = [
]

for i in range(len(questions)):
    quiz.append(dict(Question = questions[i], Choices = choices[i], Answer = answers[i]))

startQuiz()
