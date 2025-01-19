# 5.8 Monthly Sales Tax
# A retail company must file a monthly sales tax report listing the total sales 
# for the month, and the amount of state and county sales tax collected. The state
# tax rate is 5 percent and the county tax rate is 2.5 percent. Write a program a 
# program that asks the user to enter the total sales for the month. From this figure,
# the application should calculate and display the following:
#  1. The amount of county sales tax
#  2. The amount of state sales tax
#  3. The amount of total sales tax

def calculate_total_sales_tax(taxes):
    return sum(taxes)

# Constants for tax rates
STATE_TAX_RATE = 0.05  # 5%
COUNTY_TAX_RATE = 0.025  # 2.5%

# Input: Total sales for the month
total_sales = float(input("Enter the total sales for the month: $"))

# Calculate taxes
county_sales_tax = COUNTY_TAX_RATE * total_sales
state_sales_tax = STATE_TAX_RATE * total_sales
total_sales_tax = calculate_total_sales_tax([county_sales_tax, state_sales_tax])

# Output
print(f"\n1. The amount of county sales tax: ${county_sales_tax:,.2f}")
print(f"2. The amount of state sales tax: ${state_sales_tax:,.2f}")
print(f"3. The amount of total sales tax: ${total_sales_tax:,.2f}")




