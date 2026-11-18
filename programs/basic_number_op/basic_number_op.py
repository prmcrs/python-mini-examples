"""Small exercises with integer arithmetic and comparisons."""


def add(a, b):
    return a + b


def multiply_three(a, b, c):
    return a * b * c


def comparisons(a, b):
    return [
        f"{a} {symbol} {b}"
        for symbol, matches in (
            ("==", a == b), ("!=", a != b), ("<", a < b),
            (">", a > b), ("<=", a <= b), (">=", a >= b)
        )
        if matches
    ]


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main():
    while True:
        print("\n1. Add two integers\n2. Compare two integers\n3. Multiply three integers\n4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "4":
            print("Goodbye!")
            break
        if choice not in {"1", "2", "3"}:
            print("Invalid option.")
            continue
        a = read_integer("First integer: ")
        b = read_integer("Second integer: ")
        if choice == "1":
            print(f"Sum: {add(a, b)}")
        elif choice == "2":
            print("\n".join(comparisons(a, b)))
        else:
            c = read_integer("Third integer: ")
            print(f"Product: {multiply_three(a, b, c)}")


if __name__ == "__main__":
    main()
