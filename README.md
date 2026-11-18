# Python Mini Examples

Small, independent command-line exercises for learning Python, adapted from programs originally written in C. The goal is to compare familiar programming concepts across the two languages without adding unnecessary frameworks.

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

## Learning from C to Python

These ports demonstrate Python's indentation-based blocks, `print()` and `input()` instead of `printf()` and `scanf()`, `range()` instead of C-style loop counters, and functions without mandatory type declarations. The goal is readable, introductory code rather than the shortest possible solution.

See each example's README for behavior and C-to-Python learning notes. Original C source files are not included unless verified; these Python files should not be mistaken for verbatim translations.

## Add an example

Create `programs/<example>/<example>.py` with a `main()` function and a `if __name__ == "__main__": main()` guard. Add a friendly label and module path to `PROGRAMS` in `main.py`, document the exercise, and add tests for calculation functions.

## Emissions status

The emissions example is unfinished. It currently computes carbon monoxide (CO) grams per mile using a configurable comparison threshold (default: 3.4 g/mi). Vehicle class is collected but does not affect the calculation. This is an exercise threshold, not a statement of regulatory compliance. The program does **not** calculate CO₂ or fuel consumption yet.
