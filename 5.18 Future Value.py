# 5.18 Future Value. 
# Suppose you have a certain amount of money in a savings account that earns compound
# monthly interest, and you want to calculate the amount that you will have after a 
# specific number of months. The formula is as follows:

# F = P x (1+i)**t

# The terms in the formula are:
# F is the future value of the account after the specified time period.
# P is the present value of the account.
# i is the monthly interest rate.
# t is the number of months.

# Write a program that prompts the user to enter the account's present value,
# monthly interest rate, and the number of months that the money will be left
# in the account. The program should pass these values to a function that returns
# value of the account, after the specified number of months. The program should
# display the account's future value.

def calculate_future_value(present, interest, months):
    """
    Calculate the future value of the account.
    :param present: Present value of the account
    :param interest: Monthly interest rate (as a percentage)
    :param months: Number of months the money will be left in the account
    :return: Future value of the account
    """
    return present * (1 + interest / 100) ** months

# Input from the user
present = float(input("Enter the present value of the account: $"))
interest = float(input("Enter the monthly interest rate (%): "))
months = int(input("Enter the number of months: "))

# Calculate future value
future = calculate_future_value(present, interest, months)

# Display the result
print(f"The account's future value: ${future:,.2f}")
