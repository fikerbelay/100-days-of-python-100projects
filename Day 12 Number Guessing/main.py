from random import randint

from art import logo
import random

number = randint(1, 100)


print(logo)

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


def status(guess, tries):

    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print(f"You got it! the answer was {guess}")
        exit()

    if tries >= 1:
        print(f"You have {tries} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses. refresh the page to run again.")


if difficulty == "easy":
    tries = 10
    print(f"You have {tries} attempts remaining to guess the number.")

    while tries >= 1:
        tries -= 1
        guess = int(input("Make a guess: "))
        status(guess, tries)


elif difficulty == "hard":
    tries = 5
    print(f"You have {tries} attempts remaining to guess the number.")

    while tries >= 1:
        tries -= 1
        guess = int(input("Make a guess: "))
        status(guess, tries)

else:
    print("Wrong entry. please run the program again.")