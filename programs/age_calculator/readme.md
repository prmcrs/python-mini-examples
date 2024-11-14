# Age Calculator

## Description

This program calculates a person's age based on their date of birth. It takes the user's birthdate as input and calculates the age in years, months, and days, considering the current date. The program handles leap years and adjusts for any date discrepancies to ensure an accurate age calculation.

## Structure

- **age_calculator.py**: Contains the core functionality for calculating age based on the user's input.
- **main.py**: The entry point to run the program and interact with the user.

## How It Works

1. The user enters their date of birth in the format (YYYY-MM-DD).
2. The program calculates the age by comparing the current date with the birthdate.
3. The age is displayed in years, months, and days.

## Running the Program

To run this program from the main menu (main.py), follow these steps:
1. Run the `main.py` file from the project root:
   - `python main.py`
2. Select the option corresponding to "Age Calculator" in the menu (option number 2 if configured in `main.py`).
3. Enter your date of birth when prompted.

## Example Usage

Assuming the user's date of birth is January 15, 1990:

- Enter your date of birth (YYYY-MM-DD): 1990-01-15

Output:
- Your age is: 34 years, 10 months, and 29 days.

## Notes
- The program accounts for leap years and adjusts the calculation accordingly.
- The program assumes the user's input is in the correct format (YYYY-MM-DD). 

## Requirements
- Python 3.x

## Credits
This program was developed to demonstrate simple date manipulation and age calculation using Python.
