import random

print("Welcome to Guess My Number Game!")

# Random number between 1 and 100
number = random.randint(1, 100)

guess = None
attempts = 0

while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number.")
        print("Total attempts:", attempts)