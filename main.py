import os
import importlib

# Dictionary of program options and their module paths
programs = {
    "1": "programs.prime.prime",
    "2": "programs.function_xxx.function_xxx",
    # Add more programs here as you add them
}

def show_menu():
    print("Select a program to execute:")
    for key, value in programs.items():
        print(f"{key}. {value.split('.')[-1]}")

def run_program(option):
    try:
        module = importlib.import_module(programs[option])
        module.main()
    except KeyError:
        print("Invalid option.")
    except AttributeError:
        print("The selected program does not have a main() function.")

if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Enter the program number to execute (or 'q' to quit): ")
        if option.lower() == 'q':
            break
        run_program(option)
