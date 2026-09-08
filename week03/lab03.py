import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"Once upon a time, a {adjective} {noun} decided to {verb} across the kingdom."


def guessing_game():
    """Run an interactive number-guessing game."""
    secret = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("Correct!")
            break