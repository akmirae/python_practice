# 3.10 Money Counting Game
# Create a change-counting game that gets the user to enter the number of coins required 
# to make exactly one dollar. The program should prompt the user to enter the number of 
# pennies, nickels, dimes, and quarters. If the total value of the coins entered is 
# equal to one dollar, the program should congratulate the user for winning the game. 
# Otherwise, the program should display a message indicating whether the amount entered 
# was more than or less than one dollar.

# Create constants.
penny = .01
nickel = .05
dime = .1
quarter = .25

try:
    # Ask the user input the number of pennies, nickels, dimes and quarters to make one dollar.
    pennies = int(input("Enter the number of pennies: "))
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))
    
    total_value = penny * pennies + nickel * nickels + dime * dimes + quarter * quarters
    
    # if the numbers of coins are negative, display error message.
    if pennies < 0 or nickels < 0 or dimes < 0 or quarters < 0:
        print("\nError: The numbers of coins cannot be negative values.")
    else:
        # Calculate the coins' value and display the result.
        if total_value == 1:
            print("\nCongratulations!!! You win the game.")
        elif total_value < 1:
            print(f"\nThe value you enter is ${total_value:,.2f}. The value is less than one dollar.") 
        else:
            print(f"\nThe value you enter is ${total_value:,.2f}. The value is more than one dollar.") 
except ValueError:
    print('\nInvalid Input. Enter numeric values for the numbers of coins')
