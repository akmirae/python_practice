# 5.6 Stadium Seating
# There are three seating categories at a stadium. Class A seats cost $20,
# Class B seats cost $15, and Class C seats cost $10. Write a program that asks
# how many tickets for each class of seats were sold, then displays the amount 
# of income generated from ticket sales.

# Function to calculate total ticket sales
def calculate_ticket_sales(sales):
    return sum(sales)

# Prompt the user for the number of tickets sold for each class
classA = int(input("How many tickets for Class A were sold? "))
classB = int(input("How many tickets for Class B were sold? "))
classC = int(input("How many tickets for Class C were sold? "))

# Define ticket prices
price_classA = 20
price_classB = 15
price_classC = 10

# Calculate sales for each class
sales_classA = price_classA * classA
sales_classB = price_classB * classB
sales_classC = price_classC * classC

# Store the sales in a list
sales = [sales_classA, sales_classB, sales_classC]

# Calculate total ticket sales
total_sales = calculate_ticket_sales(sales)

# Display the results
print(f"\nIncome generated from Class A ticket sales: ${sales_classA:,.2f}")
print(f"Income generated from Class B ticket sales: ${sales_classB:,.2f}")
print(f"Income generated from Class C ticket sales: ${sales_classC:,.2f}")
print(f"\nThe total ticket sales is: ${total_sales:,.2f}")
