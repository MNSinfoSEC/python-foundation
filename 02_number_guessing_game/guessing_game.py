# Number Guessing Game
# Python Foundation - Project 02

import random

secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")

    elif guess > secret_number:
        print("Too high! Try again.")

    else:
        print("🎉 Correct! You guessed it in {attempts} attempts.")
        break
