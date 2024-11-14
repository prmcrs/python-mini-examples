# programs/emissions/emissions.py

def calculate_co_emission(committed, miles, max_co=3.4):
    co_rate = committed / miles
    meets_emission = co_rate <= max_co
    return co_rate, meets_emission

def main():
    car_class = input("Enter vehicle class (C)ompact (I)ntermediate (S)tandard (L)uxury): ")
    committed = float(input("Enter amount of carbon monoxide emitted (grams): "))
    miles = float(input("Enter miles driven during test: "))

    co_rate, meets_emission = calculate_co_emission(committed, miles)
    max_co = 3.4  # Máximo g/mi permitido

    print(f"Carbon monoxide emission of {co_rate:.2f} g/mi. ", end="")
    if meets_emission:
        print("meets ", end="")
    else:
        print("exceeds ", end="")
    print(f"permitted emission of {max_co} g/mi.")

if __name__ == "__main__":
    main()
