'''
We created another function to make the drawBox function more 'clean'. The printBoxLine draws one
line of the box, n times.
'''

def drawBox(length):
    for j in range(length):
        printBoxLine(length, "*------", "*", 1)
        printBoxLine(length, "|      ", "|", 2)
    printBoxLine(length, "*------", "*", 1)


def printBoxLine(length, char1, char2, n):
    for j in range(n):
        print(char1 * length + char2)


drawBox(5)
