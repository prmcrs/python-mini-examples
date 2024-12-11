# programs/prime/prime.py

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_factors(number):
    factors = []
    divisor = 2
    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    return factors

def primes_up_to(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    while True:
        try:
            print("\nOptions:")
            print("1. Check if a number is prime")
            print("2. List all primes up to a number")
            print("3. Find the prime factorization of a number")
            print("4. Exit")
            choice = int(input("Choose an option: "))

            if choice == 1:
                number = int(input("Enter a number to check: "))
                if is_prime(number):
                    print(f"{number} is a prime number.")
                else:
                    print(f"{number} is not a prime number.")
            elif choice == 2:
                limit = int(input("Enter the upper limit: "))
                primes = primes_up_to(limit)
                print(f"Primes up to {limit}: {primes}")
            elif choice == 3:
                number = int(input("Enter a number to factorize: "))
                factors = prime_factors(number)
                print(f"Prime factors of {number}: {factors}")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
