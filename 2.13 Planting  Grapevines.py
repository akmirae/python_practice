# 2.13 Planting  Grapevines
# A vineyard owner is planting several new rows of grapevines, and needs to know how many 
# grapeviens to plant in each row. She has determined that after measuring the length of a 
# future row, she can use the following formula to calculate the number of vines that will 
# fit in the row, along with the trellis end-post assemblies that will need to be constructed 
# at each end of the row:
# V = (R-2E)/S
# The terms in the formula are:
# V is the number of grapevines that will fit in the row.
# R is the length of the row, in feet.
# E is the amount of space, in feet, used by an end-post assembly.
# S is the space between vines, in feet.
# Write a program that makes the calculation for the vineyard owner. The program should ask the
# user to input the following: 
#  * The length of the row, in feet 
#  * The amount of space used by an end-post assembly, in feet 
#  * The amount of space between the vines, in feet 
# Once the input data has been entered, the program should calculate and display the number of 
# grapevines that will fit in the row.
# Ask an user to input data.
import math

try:
    length_row = float(input("Enter the length of the row(in feet): "))
    end_space = float(input("Enter the amount of space for end-post(in feet): "))
    vines_space = float(input("Enter the space between vines(in feet): "))
    
    # Calculate the numer of grapevines the owner wants to plant.
    vines_number = math.floor((length_row - 2 * end_space) / vines_space)
    
    # Show error message for negative values.
    if length_row < 0 or end_space < 0 or vines_space <0 :
        print("Error: Your input data cannot be negative value.")
    else:
        print(f"The number of grapevines you can plant is '{vines_number} grapevines'.")
        
except ValueError:
    print("Invalid Input. Please enter positive numeric value for input data.")
