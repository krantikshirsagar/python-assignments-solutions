# Mini Project 5: Number Guessing Game
# Problem Statement: Give the user a limited number of chances to guess a secret number.
# Rules: secret 37, max 5 guesses, Too low/Too high hints, stop on correct, reveal secret if all fail.

secret = 37
max_guesses = 5
attempts = 0
guessed = False

while attempts < max_guesses:
    guess = int(input(f"Guess {attempts + 1}/{max_guesses} - Enter a number: "))
    attempts = attempts + 1
    if guess == secret:
        print("Congratulations! You guessed correctly.")
        guessed = True
        break
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")

print("Attempts used:", attempts)
if not guessed:
    print(f"You lost! The secret number was {secret}")
else:
    print("Result: Win")
