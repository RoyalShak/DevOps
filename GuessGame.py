
import random


def play(difficulty):
    rama = difficulty
    secret = random.randint(1, int(rama))
    guess = None
    while guess != secret:
        guess = input(f"Please choose a number between 1 to {rama} :")
        if guess.isdigit():
            guess = int(guess)
        if guess == secret:
            print("Holy Shit You DiD IT!!")
        else:
            print("Please try again")
    print("Well Done!!")
    return
