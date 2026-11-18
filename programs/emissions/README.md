# Emissions Calculator — Work in Progress

Calculates carbon monoxide (CO) grams per mile from total grams emitted and miles driven. Compares the result with an exercise threshold of 3.4 g/mi. Vehicle class is requested but does not change the formula yet. This is not a CO₂ calculator or a regulatory certification tool.

## Run

From the repository root:

```bash
python programs/emissions/emissions.py
```

Or choose the exercise from `python main.py`.

## From C to Python

Floating-point arithmetic, division, units and input validation. The vehicle-specific rules are not implemented yet. Python uses indentation for blocks, `input()` for terminal input and `print()` for output. Compare these concepts with C's braces, `scanf()` and `printf()`.

## Remaining work

Vehicle-class-specific behavior and the original exercise's intended rules still need to be confirmed. No assumptions about legal limits or CO₂ calculations are made.
