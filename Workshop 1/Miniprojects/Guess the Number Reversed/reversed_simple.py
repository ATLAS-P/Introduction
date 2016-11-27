from math import floor

def guess(min, max, reply = ''):
    if reply != 'c':
        new_guess = floor((min + max + 1) / 2)

        print(new_guess)
        reply = input()

        guess(new_guess if reply == 'h' else min,
              new_guess if reply == 'l' else max,
              reply)

guess(0, int(input()))