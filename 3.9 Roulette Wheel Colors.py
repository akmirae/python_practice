# 3.9 Roulette Wheel Colors
# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets
# are as follows:
#  * Pocket 0 is green.
#  * For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered 
#   pockets are black
#  * For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered 
#   pockets are red
#  * For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered 
#   pockets are black
#  * For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered 
#   pockets are red.

# Write a program that asks the user to enter a pocket number and displays whether the pocket
# is greed, red, or black. The program should display an error message if the user enters 
# a number that is outside the range of 0 through 36.

try:
    # Ask the user input a pocket number for the pocket color.
    number = int(input("Enter a pocket number from 0 to 36: "))
    
    # Error messages for outside the range.
    if number < 0 or number > 36:
        print("Error: the number should be from 0 to 36.")
    elif number == 0:
        print(f"\nThe pocket color for {number} is 'green'. ")
    else:
        if 1 <= number <=10 or 19 <= number <= 28:
            color = "red" if number % 2 != 0 else "black"
        elif 11 <= number <=18 or 29 <= number <= 36:
            color ="black" if number % 2 != 0 else "red"
        print(f"\nThe pocket color for '{number}' is '{color}'. ")
        
except ValueError:
    print("Invalid Input. Please enter a numeric value from 0t o 36 for the pocket color.")