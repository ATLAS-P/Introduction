import random

N = random.randint(1, 100)


def get_guess():
    guess = int(input("What's your guess, sir? "))

    if guess == N:
        print("Whoo! That's correct!")
    elif guess < N:
        print("Oops. That's too small.")
    else:
        print("Oops. That's too large.")


get_guess()
get_guess()
get_guess()
get_guess()
# ...
