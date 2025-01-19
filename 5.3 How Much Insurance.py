# 5.3 How Much Insurance?
# Many financial experts advise that property owners should insure their homes or
# buildings for at least 80 percentage of the amount it would cost to replace the structure.
# Write a program that asks the user to enter the replacement cost of a building, then
# displays the minimum amount of insurance he or she should buy for the property.

# Function to calculate the minimum insurance amount
def calculate_insurance(replacement_cost):
    return replacement_cost * 0.8

# Prompt the user for input
replacement_cost = float(input("Enter the replacement cost of a building: $"))

# Calculate the minimum insurance amount
minimum_insurance = calculate_insurance(replacement_cost)

# Display the result
print(f"The minimum amount of insurance you should buy for the property is: ${minimum_insurance:,.2f}")

