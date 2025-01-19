# 3.6 Magic Dates
# The date June 10, 1960, is special because when it is written in the following format, 
# the month times the day equals the year:
# 6/10/60
# Design a program that asks the user to enter a month (in numeric form), a day, and 
# a two-digit year. The program should then determine whether the month times the day 
# equals the year. If so, it should display a message saying the date is magic. Otherwise, 
# it should display a message saying the date is not magic.

try:
    # Ask the user to input a month (in numeric form), a day, and a two-digit year.
    month = int(input("Enter a month(in numeric form, eg. 1,2,3): "))
    day = int(input("Enter a day: "))
    year = int(input("Enter a two-digit year(eg 2014 -> 14): "))
    
    # Ensure the year is two digits
    if year < 0 or year > 99:
        print("Error: The year should be a two-digit number.")
    else:
        # Calculate the data and determine if it is a magic date and display the result.
        date = month * day
        if month < 1 or day < 1:
            print("Error: day and month cannot be 0 or negative values.")
        elif date == year:
            print(f"\nThe date '{month}/{day}/{year}' is magic.")
        else:
            print(f"\nThe date '{month}/{day}/{year}' is not magic.")
        
except ValueError:
    print('Invalid Input. Please enter positive integers for the month, day and year.')
        