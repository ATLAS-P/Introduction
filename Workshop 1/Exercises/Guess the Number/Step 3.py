import random

guessed = False
N = random.randint(1, 100)


def get_guess():
    global guessed

    guess = int(input("What's your guess, sir? "))

    if guess == N:
        print("Whoo! That's correct!")
        guessed = True
    elif guess < N:
        print("Oops. That's too small.")
    else:
        print("Oops. That's too large.")


for i in range(7):
    if guessed:
        break

    get_guess()
