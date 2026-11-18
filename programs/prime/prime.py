"""Simple prime-number exercises."""
from math import isqrt


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            return False
    return True


def prime_factors(number):
    """Return factors for integers >= 2; 0, 1 and negatives are unsupported."""
    if number < 2:
        raise ValueError("Prime factorization requires an integer >= 2.")
    factors = []
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    return factors


def primes_up_to(limit):
    return [number for number in range(2, limit + 1) if is_prime(number)]


def main():
    while True:
        print("\n1. Check prime\n2. List primes\n3. Prime factorization\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        if choice not in {"1", "2", "3"}:
            print("Invalid option.")
            continue
        try:
            number = int(input("Enter an integer: "))
            if choice == "1":
                print(f"{number} is {'prime' if is_prime(number) else 'not prime'}.")
            elif choice == "2":
                print(f"Primes up to {number}: {primes_up_to(number)}")
            else:
                print(f"Prime factors of {number}: {prime_factors(number)}")
        except ValueError as error:
            print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
