import re

question = re.split(r'\d+', open(r'C:\Users\monfa\Documents\GitHub\Warming-Up\Beginner_Python\Simple Quiz Game Files\Questions.txt').read())
answers = open(r'C:\Users\monfa\Documents\GitHub\Warming-Up\Beginner_Python\Simple Quiz Game Files\Answers.txt').read().splitlines()

print (question)
print (answers)