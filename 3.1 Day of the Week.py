# 3.1 Day of the Week.
# Write a program that asks the user for a number in the range of 1 through 7. The 
# program should display the corresponding day of the week, where 1 = Monday, 
# 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. 
# The program should display an error message if the user enter a number that is 
# outside the range of 1 through 7.

# Ask the user to input a number in the range of 1 to 7.
try:
    number = int(input("Enter a number in the range of 1 through 7: "))

    # Assign day of week based on the number the user enter.


    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")
    elif number == 7:
        print("Sunday")
    else:
        print("Error: You should input an integer between 1 to 7")
        
except ValueError:
    print("Invalid Input. Please enter an integer value between 1 to 7")