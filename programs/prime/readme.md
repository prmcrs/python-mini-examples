# Prime Number Checker

## Description

This program checks if a given number is a prime number. A prime number is a number greater than 1 that cannot be formed by multiplying two smaller natural numbers. The program takes an integer as input and determines whether it is prime or not.

## Structure

- **prime.py**: Contains the code to check if a number is prime.
- **main.py**: The entry point to run the program and interact with the user.

## How It Works

1. The user enters a number when prompted.
2. The program checks if the number is divisible by any integer other than 1 and itself.
3. If no divisors are found, the number is prime; otherwise, it is not.

## Running the Program

To run this program from the main menu (main.py), follow these steps:
1. Run the `main.py` file from the project root:
   - `python main.py`
2. Select the option corresponding to "Prime Number Checker" in the menu (option number 1 if configured in `main.py`).
3. Enter a number when prompted to check if it's prime.

## Example Usage

Assuming the user enters the number 29:

- Enter a number: 29

Output:
- 29 is a prime number.

For a non-prime number, such as 30:

- Enter a number: 30

Output:
- 30 is not a prime number.

## Notes
- The program checks divisibility starting from 2 up to the square root of the number, optimizing the process.
- The program assumes the user will input a valid integer.

## Requirements
- Python 3.x

## Credits
This program was developed to demonstrate prime number checking in Python.
