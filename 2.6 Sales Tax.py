# 2.6 Sales Tax
# Write a program that will ask the user to enter the amount of a purchase. The program should 
# then compute the state and county sales tax.
# state sales tax: 5% , county sales tax: 2.5%
# The program should display the amount of the purchase, the state sales tax, the county sales tax,
# and the total of the sale.

state_sales_tax_rate = 0.05
county_sales_tax_rate = 0.025

try:
    purchase_amount = float(input("Enter your purchase amount: "))
    if purchase_amount < 0:
        print("The input cannot be negative. Please enter a positive number.")
    else:
        state_sales_tax = purchase_amount * state_sales_tax_rate
        county_sales_tax = purchase_amount * county_sales_tax_rate
        total_sales_amount = purchase_amount + state_sales_tax + county_sales_tax
        print("\n*** Total sales amount of the purchase ***")
        print("=" * 40)
        print(f"Purchase Amount:            ${purchase_amount:,.2f}")
        print(f"State Sales Tax (5%):       ${state_sales_tax:,.2f}")
        print(f"County Sales Tax(2.5%):     ${county_sales_tax:,.2f}")
        print(f"Total Amount (with taxes):  ${total_sales_amount:,.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric input.")
