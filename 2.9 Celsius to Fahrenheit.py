# 2.9 Celsius to Fahrenheit
# Write a program that converts Celsiun temperatures to Fahrenheit temperatures. The formula is
# as follows:  F = 9C/5 + 32
# The program should ask the user to enter a temperature in Celsius, then display the temperature
# converted to Fahrenheit.
temperature_constant = 32
try:
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (9*celsius)/5 + temperature_constant
    print("\n**** Celsius To Fahrenheit *****")
    print("=" * 40)
    print(f"{'Celsius':<15} {celsius:>10,.2f} C ")
    print(f"{'Fahrenheit':<15} {fahrenheit:>10,.2f} F")
    
except ValueError:
    print("Invalid Input. Please enter a numeric values for celsius.")
