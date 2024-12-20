import os
import importlib

# Dictionary of program options and their module paths
programs = {
    "1": "programs.hello_world.hello_world",
    "2": "programs.prime.prime",
    "3": "programs.age_calculator.age_calculator",
    "4": "programs.emissions.emissions",  
    "5": "programs.guess_number.guess_number", 
    "6": "programs.basic_number_op.basic_number_op",
}

def show_menu():
    print("Select a program to execute:")
    for key, value in programs.items():
        # Display the program name from the module path
        print(f"{key}. {value.split('.')[-1]}")

def run_program(option):
    try:
        # Import the module dynamically based on user selection
        module = importlib.import_module(programs[option])
        # Execute the main function of the selected module
        module.main()
    except KeyError:
        print("Invalid option.")
    except AttributeError:
        print("The selected program does not have a main() function.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        show_menu()
        option = input("Enter the program number to execute (or 'q' to quit): ")
        if option.lower() == 'q':
            print("Exiting the program. Goodbye!")
            break
        run_program(option)
