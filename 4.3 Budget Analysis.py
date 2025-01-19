# 4.3 Budget Analysis
# Write a program that asks the user to enter the amount that they have budgeted for 
# a month. A loop should then prompt the user to enter each of their expenses for 
# the month and keep a running total. When the loop finishes, the program should display 
# the amount that the user is over or under budget.

# Initialize total expense.
total_expense = 0

# Ask the user to enter the budget amount for a month.
budget = float(input("Enter the monthly budget: $"))

# Continuously ask for expenses
while True:
    # Ask for expense details.
    expense_name = input("Enter the expense name: ")
    expense_amount = float(input(f"The amount of the {expense_name}: $"))
    
    # Add to the running total of expenses.
    total_expense += expense_amount    
    
    # Check if the user wants to add more expenses
    more_items = input("Do you want more items to enter? (y/n)").lower()
    if more_items == 'n':
        break

# Display the results
print(f"The budget: ${budget:,.2f}")
print(f"The total expenses: ${total_expense:,.2f}")

# Check if over, under, or on budget.
if budget > total_expense:
    print(f"Your budget is over the total expense by {budget - total_expense:,.2f}")
elif budget < total_expense:
    print(f"Your budget is under the total expense by {total_expense - budget:,.2f}")
else:
    print("Your budget is equal to the total expense.")


    
    
    
    
    
