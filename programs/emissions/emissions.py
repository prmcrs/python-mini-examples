"""Work in progress: simple CO emissions exercise (grams per mile).

The vehicle class is collected for a future extension, but does not yet
change the calculation. The 3.4 g/mi threshold is an exercise default,
not a universal regulatory limit.
"""
from math import isfinite

DEFAULT_MAX_CO = 3.4
VEHICLE_CLASSES = {"C": "Compact", "I": "Intermediate", "S": "Standard", "L": "Luxury"}


def calculate_co_emission(committed, miles, max_co=DEFAULT_MAX_CO):
    if not all(isfinite(value) for value in (committed, miles, max_co)):
        raise ValueError("Values must be finite numbers.")
    if committed < 0:
        raise ValueError("CO emitted cannot be negative.")
    if miles <= 0:
        raise ValueError("Miles must be greater than zero.")
    if max_co < 0:
        raise ValueError("The emission limit cannot be negative.")
    co_rate = committed / miles
    return co_rate, co_rate <= max_co


def main():
    car_class = input("Enter vehicle class (C)ompact (I)ntermediate (S)tandard (L)uxury: ").strip().upper()
    if car_class not in VEHICLE_CLASSES:
        print("Invalid vehicle class.")
        return
    try:
        committed = float(input("Enter carbon monoxide emitted (grams): "))
        miles = float(input("Enter miles driven during test: "))
        co_rate, meets_emission = calculate_co_emission(committed, miles)
    except ValueError as error:
        print(f"Invalid input: {error}")
        return
    status = "meets" if meets_emission else "exceeds"
    print(f"{VEHICLE_CLASSES[car_class]} vehicle: {co_rate:.2f} g/mi; "
          f"{status} the exercise threshold of {DEFAULT_MAX_CO} g/mi.")
    print("Note: vehicle class does not affect the calculation yet (work in progress).")


if __name__ == "__main__":
    main()
