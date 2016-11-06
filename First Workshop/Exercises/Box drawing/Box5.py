'''
By encapsulating the code inside a function we can reuse it when we need it. Furthermore,
the code has been made more general with the parameter length, which determines the
amount of amount of 'sub' boxes in our box (just run it).
'''


def drawBox(length):
    for i in range(length):
        print("*------" * length + "*")

        for j in range(2):
            print("|      " * length + "|")

    print("*------" * length + "*")


drawBox(4)
drawBox(12)
drawBox(8)
