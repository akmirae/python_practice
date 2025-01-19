# 3.4 Roman Numerals
# Write a program that prompts the user to enter a number within the range of 1 through 10.
# The program should display the Roman numeral version of that number.
# If the number is outside the range of 1 through 10, the program should display an error message.
# The following table shows the Roman numerals for the numbers 1 through 10:

# Ask the user to input a number within the range of 1 through 10.
try:
    number = int(input("Enter a number(1 to 10): "))

    # Convert to Roman Numerals and display the result.
    if number < 1 or number > 10:  # Display "out of range error message"
        print("Error: the number you entered is outside the range of 1 to 10.")
    elif number == 1:   # I, II, III, IV, V, VI, VII, VIII, IX, X 
        print("The Roman Numeral for 1 is I.")
    elif number == 2:
        print("The Roman Numeral for 2 is II.")
    elif number == 3:
        print("The Roman Numeral for 3 is III.")
    elif number == 4:
        print("The Roman Numeral for 4 is IV.")
    elif number == 5:
        print("The Roman Numeral for 5 is V.")
    elif number == 6:
        print("The Roman Numeral for 6 is VI.")
    elif number == 7:
        print("The Roman Numeral for 7 is VII.")
    elif number == 8:
        print("The Roman Numeral for 8 is VIII.")
    elif number == 9:
        print("The Roman Numeral for 9 is IX.")     
    else:    
        print("The Roman Numeral for 10 is X.")
except ValueError:
    print("Invalid Input. Please enter numeric value 1 through 10 for the number.")