# 5.4 Automobile Costs
# Write a program that asks the user to enter the monthly costs for the following expenses
# incurred from operating their automobile: loan payment, insurance, gas, oil, tires, and 
# maintenance. The program should then display the total monthly cost of these expense, and 
# the total annual cost of these expenses.

# Function to calculate total monthly cost
def calculate_total_monthly_cost(expenses):
    return sum(expenses)

# Prompt the user to enter monthly expenses
loan_payment = float(input("Enter your monthly loan payment: $"))
insurance = float(input("Enter your monthly insurance cost: $"))
gas = float(input("Enter your monthly gas cost: $"))
oil = float(input("Enter your monthly oil cost: $"))
tires = float(input("Enter your monthly tires cost: $"))
maintenance = float(input("Enter your monthly maintenance cost: $"))

# List of expenses
expenses = [loan_payment, insurance, gas, oil, tires, maintenance]

# Calculate total monthly and annual costs
total_monthly_cost = calculate_total_monthly_cost(expenses)
total_annual_cost = total_monthly_cost * 12

# Display the results
print(f"\nTotal monthly cost of automobile expenses: ${total_monthly_cost:,.2f}")
print(f"Total annual cost of automobile expenses: ${total_annual_cost:,.2f}")
