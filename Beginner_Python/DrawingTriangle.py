def drawingSpaces(lineNumber):
    print(lineNumber * ' ', end='')

def numOfChar(height, lineNumber):
    return 2 * (height-lineNumber) - 1

def drawingChar(character, height, lineNumber):
    print(character * numOfChar(height, lineNumber))    

def drawingTriangle(height, character):
    for line in range(height):
        drawingSpaces(line)
        drawingChar(character, height, line)

if __name__ == '__main__':
    triangleHeight = int(input("What is the height of the triangle? "))
    character = str(input("What characters do you want the triangle to be drawn out of? "))
    drawingTriangle(triangleHeight, character)