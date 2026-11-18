# Python Mini Examples

```plaintext
╔╦╗╦ ╦╦╔═╗  ╦╔═╗  ╔═╗╦ ╦╔╦╗╦ ╦╔═╗╔╗╔  ┬┬
 ║ ╠═╣║╚═╗  ║╚═╗  ╠═╝╚╦╝ ║ ╠═╣║ ║║║║  ││
 ╩ ╩ ╩╩╚═╝  ╩╚═╝  ╩   ╩  ╩ ╩ ╩╚═╝╝╚╝  oo
```

This repository contains a collection of small, independent command-line programs for learning and practicing Python. Each example focuses on fundamental concepts such as variables, loops, functions, conditions, user input, and basic algorithms. Some exercises were originally written in C and later adapted to Python.

## Examples

| Menu | Example | Concepts |
| --- | --- | --- |
| 1 | Hello World | Printing, raw strings, ASCII art |
| 2 | Prime Numbers | Functions, loops, divisibility, integer square roots |
| 3 | Age Calculator | Dates, validation, conditional expressions |
| 4 | Emissions Calculator **(work in progress)** | Division, units, validation |
| 5 | Guess the Number | Random numbers, loops, input handling |
| 6 | Basic Number Operations | Arithmetic, comparisons, functions |

## Run

Requires Python 3.8 or later; no third-party dependencies.

```bash
git clone https://github.com/prmcrs/python-mini-examples.git
cd python-mini-examples
python main.py
```

Each exercise can also run independently:

```bash
python programs/prime/prime.py
```

Run the standard-library tests:

```bash
python -m unittest discover -s tests -v
```

## Learning Python

The examples are intentionally small and easy to explore. Run them, read the code, change the inputs, and experiment with different solutions. Each program has its own README explaining what it does and which Python concepts it practices.

## Add an example

Create `programs/<example>/<example>.py` with a `main()` function and a `if __name__ == "__main__": main()` guard. Add a friendly label and module path to `PROGRAMS` in `main.py`, document the exercise, and add tests for calculation functions.

## Emissions status

The emissions example is unfinished. It currently computes carbon monoxide (CO) grams per mile using a configurable comparison threshold (default: 3.4 g/mi). Vehicle class is collected but does not affect the calculation. This is an exercise threshold, not a statement of regulatory compliance. The program does **not** calculate CO₂ or fuel consumption yet.
