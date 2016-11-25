


# different ways to loop
def printN_for(n, str):
    for i in range(n):
        print(str)


def printN_while(n, str):
    while n >= 0:
        print(str)
        n -= 1

def printN_recursion(n, str):
    if n >= 0:
        print(str)
        printN_recursion(n - 1, str)


printN_for(3, "Hello, For!")
printN_for(3, "Hello, While!")
printN_for(3, "Hello, Recursion!")

