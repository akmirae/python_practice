# 2.7 Miles-per-Gallon
# A car's miles-per-gallon(MPG) can be calculated with the following formula:
# MPG = Miles driven / Gallons of gas used
# Write a program that asks the user for the number of miles driven and the gallons of gas used.
# It should calculate the car's MPG and display the result.



try:
    miles_driven = float(input("Enter the number of miles driven: "))
    gallons_used = float(input("Enter the number of gallons used: "))
    mpg = miles_driven / gallons_used
    
    if miles_driven < 0 or gallons_used < 0:
        print("Error: The miles driven and the gallons used cannot be negative. Please enter positive numbers.")
    else:
        print(f"The car's MPG: {mpg:,.2f} miles per gallon.")
        
except ValueError:
    print("Invalid input. Please enter numeric values for miles driven and gallons used.")
        