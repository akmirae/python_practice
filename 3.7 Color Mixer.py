# 3.7 Color Mixer
# The colors red, blue, and yellow are known as the primary colors because they cannot 
# be made by mixing other colors. When you mix two primary colors, you get a secondary 
# color, as shown here:
# When you mix red and blue, you get purple.
# When you mix red and yellow, you get orange.
# When you mix blue and yellow, you get green.

# Design a program that prompts the user to enter the names of two primary colors to mix. 
# If the user enters anything other than "red," "blue," or "yellow," the program should 
# display an error message. Otherwise, the program should display the name of the 
# secondary color that results.

# Ask the user to input two colors.
color1 = input("Enter a primary color(red, blue, yellow): ").lower()
color2 = input("Enter another primary color(red, blue, yellow): ").lower()

# Display error messages when the user input colors other than primary colors, and 
# display the result of the mixed colors.
if color1 == 'red':
    if color2 == 'blue':
        print("\nThe secondary color is purple.")
    elif color2 == 'yellow':
        print("\nThe secondary color is orange.")
    else:
        print("\nError: The color should be blue or yellow.")
elif color1 == 'blue':
    if color2 == 'red':
        print("\nThe secondary color is purple.")
    elif color2 == 'yellow':
        print("\nThe secondary color is green.")
    else:
        print("\nError: The color should be red or yellow.") 
elif color1 == 'yellow':
    if color2 == 'red':
        print("\nThe secondary color is orange.")
    elif color2 == 'blue':
        print("\nThe secondary color is green.")
    else:
        print("\nError: The color should be red or blue.")
else:
    print("\nError: Please enter two primary colors for the result.")       