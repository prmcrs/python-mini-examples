# Emissions Calculator

## Description

This program calculates the carbon dioxide (CO₂) emissions of a vehicle based on the distance traveled and the type of fuel used. It allows the user to input information about their trip distance and fuel type (gasoline or diesel) and returns the estimated amount of emissions in kilograms of CO₂..

## Structure

- **emissions.py**: Contains the code for calculating carbon emissions.

## How It Works

1. The user enters the distance traveled in kilometers.
2. They select the fuel type (gasoline or diesel).
3. The program uses a default emission factor to calculate the amount of CO₂ emitted, based on the fuel type:
 - Gasoline: 2.31 kg CO₂ per liter
 - Diesel: 2.68 kg CO₂ per liter
4. The program calculates and displays the total emissions in kilograms of CO₂.

## Running the Program

To run this program from the main menu (main.py), follow these steps:
1. Run the main.py file from the project root:
 - python main.py
2. Select the option corresponding to "Emissions Calculator" in the menu (option number 3 if configured in main.py).
3. Enter the values when prompted.

## Example Usage

Assuming the distance traveled is 100 km and the fuel type is gasoline:

- Enter the distance traveled in kilometers: 100
- Enter fuel type (gasoline/diesel): gasoline

Output:
- Estimated CO₂ emissions: 23.1 kg

## Notes
The emission factors are based on standard averages. Actual emissions may vary depending on the vehicle type and driving conditions.
This program is for educational purposes only and should not be considered an official carbon emissions calculation tool.

## Requirements
Python 3.x

## Credits
This program was developed to demonstrate simple carbon emissions calculations in Python.