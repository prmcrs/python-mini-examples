"""Guess a random number from 1 to 1000."""
import random


def generate_number():
    return random.randint(1, 1000)


def main():
    print("I'm thinking of a number between 1 and 1000.")
    while True:
        secret = generate_number()
        attempts = 0
        while True:
            try:
                guess = int(input("Your guess (1-1000): "))
            except ValueError:
                print("Please enter a whole number.")
                continue
            if not 1 <= guess <= 1000:
                print("Enter a number between 1 and 1000.")
                continue
            attempts += 1
            if guess == secret:
                print(f"Correct! You guessed it in {attempts} attempts.")
                break
            print("Too high." if guess > secret else "Too low.")
        if input("Play again? (y/n): ").strip().lower() not in {"y", "yes"}:
            break


if __name__ == "__main__":
    main()
