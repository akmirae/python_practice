# 3.15 February Day
# The month of February normally has 28 days. But if it is a leap year, February has 
# 29 days. Write a program that asks the user to enter a year. The program should 
# then display the number of days in February that year. Use the following criteria 
# to identify leap years:

#   1. Determine whether the year is divisible by 100. If it is, then it is a leap 
#      year if and only if it is also divisible by 400. For example, 2000 is a leap 
#      year, but 2100 is not.
#   2. If the year is not divisible by 100, then it is a leap year if and only if 
#      it is divisible by 4. For example, 2008 is a leap year, but 2009 is not.
def february_day():
    try:
        # Ask the user to enter a year.
        year = int(input("Enter a year: "))
        
        # Display error message for negative input.
        if year < 0:
            print("Error: The year cannot be negative values")
        else:
            # if the year is divisible by 100, then it is a leap year if and only if it is also 
            # divisible by 400, and display the results.
            # If the year is not divisible by 100, then it is a leap year if and only if it is 
            # divisible by 4, and display the results.
            if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0) :
                    print(f"In {year} February has 29 days.")
            else:
                    print(f"In {year} February has 28 days.")

    except ValueError:
        print("Invalid Input. Please enter a numeric value for the year.")
# Call the function
february_day()