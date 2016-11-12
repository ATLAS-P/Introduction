'''
The function has been made even more general by splitting up length into, horizontal and
vertical length.
'''


def drawBox(lengthH, lengthV, cellSize):
    for i in range(lengthV):
        printBoxLines(lengthH, cellSize, "*", "---", 1)
        printBoxLines(lengthH, cellSize, "|", "   ", cellSize)

    printBoxLines(lengthH, cellSize, "*", "---", 1)


def printBoxLines(length, cellSize, char1, char2, n):
    for i in range(n):
        print((char1 + (char2 * cellSize)) * length + char1)


drawBox(10, 3, 1)
