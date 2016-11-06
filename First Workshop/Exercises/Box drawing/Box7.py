'''
The function has been made even more general by parameterizing the size of one sub box.
'''

def drawBox(length, cellSize):
    for i in range(length):
        printBoxLines(length, cellSize, "*", "---", 1)
        printBoxLines(length, cellSize, "|", "   ", cellSize)

    printBoxLines(length, cellSize, "*", "---", 1)


def printBoxLines(length, cellSize, char1, char2, n):
    for i in range(n):
        print((char1 + (char2 * cellSize)) * length + char1)


drawBox(10, 1)
