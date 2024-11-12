# programs/age_calculator/age_calculator.py

from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year
    # Adjust if the birth date hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def main():
    birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")
        age = calculate_age(birth_date)
        print(f"You are {age} years old.")
    except ValueError:
        print("Invalid date format. Please enter the date as YYYY-MM-DD.")
