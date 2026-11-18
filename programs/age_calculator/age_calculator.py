"""Calculate age in completed years and decade of birth."""
from datetime import date, datetime


def calculate_age(birth_date, today=None):
    today = today or date.today()
    birth = birth_date.date() if isinstance(birth_date, datetime) else birth_date
    if birth > today:
        raise ValueError("Birth date cannot be in the future.")
    return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))


def calculate_decade(birth_date):
    return (birth_date.year // 10) * 10


def main():
    try:
        value = input("Enter your birth date (YYYY-MM-DD): ")
        birth_date = datetime.strptime(value, "%Y-%m-%d").date()
        print(f"You are {calculate_age(birth_date)} years old.")
        print(f"You were born in the {calculate_decade(birth_date)}s.")
    except ValueError as error:
        print(f"Invalid date: {error}")


if __name__ == "__main__":
    main()
