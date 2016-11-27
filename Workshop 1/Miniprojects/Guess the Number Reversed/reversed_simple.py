from math import floor

min = 0
max = int(input())

reply = ''

while reply != 'c':
    guess = floor((min + max + 1) / 2)

    print(guess)
    reply = input()

    if reply == 'h':
        min = guess
    elif reply == 'l':
        max = guess