"""Menu for small, independent Python exercises."""
import importlib

PROGRAMS = {
    "1": ("Hello World", "programs.hello_world.hello_world"),
    "2": ("Prime Numbers", "programs.prime.prime"),
    "3": ("Age Calculator", "programs.age_calculator.age_calculator"),
    "4": ("Emissions Calculator (work in progress)", "programs.emissions.emissions"),
    "5": ("Guess the Number", "programs.guess_number.guess_number"),
    "6": ("Basic Number Operations", "programs.basic_number_op.basic_number_op"),
}


def show_menu():
    print("\n=== PYTHON MINI EXAMPLES ===")
    for key, (name, _) in PROGRAMS.items():
        print(f"{key}. {name}")
    print("Q. Quit")


def run_program(option):
    entry = PROGRAMS.get(option)
    if entry is None:
        print("Invalid option.")
        return
    _, module_path = entry
    module = importlib.import_module(module_path)
    module.main()


def main():
    while True:
        show_menu()
        try:
            option = input("Choose an option: ").strip().lower()
            if option == "q":
                print("Goodbye!")
                break
            run_program(option)
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
