# 2.3 Land Calculation
# One acre of land is equivalent to 13,560 square feet. Write a program that asks 
# the user to enter the total square feet in a tract of land and calculates the number
# of acres in the tract.
# Hint : Divide the amount entered by 13,560 to get the number of acres.
square_feet_per_acre = 13560

try:
    land_square_feet = int(input("Enter the area of the land(square feet): "))
    land_acres = float(land_square_feet / square_feet_per_acre)

    print(f"The acres of the land '{land_square_feet:,} square feet' is" 
        f"'{land_acres:,.2f} acres'.")

except ValueError:
    print("Invalid input! Please enter a numeric value for the land area.")
    