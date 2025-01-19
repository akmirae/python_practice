# 2.4 Total Purchase
# A customer in a store is purchasing five items. Write a program that asks 
# for the price of each item, then displays the subtotal of the sale, the amount
# of sales tax, and the total. Assume the sales tax is 7 percent.

sales_tax = 0.07
item_one = float(input("Enter the first item's price: "))
item_two = float(input("Enter the second item's price: "))
item_three = float(input("Enter the third item's price: "))
item_four = float(input("Enter the fourth item's price: "))
item_five = float(input("Enter the fifth item's price: "))

subtotal_sales = item_one + item_two + item_three + item_four + item_five
total_sales_tax = subtotal_sales * sales_tax
total_price = subtotal_sales + total_sales_tax

try:
    print("\n*** The Total Price of the five items ***")
    print("=" * 40)
    print(f"The Sub total price of the sales: ${subtotal_sales:,.2f}")
    print(f"The Total sales tax amount:       ${total_sales_tax:,.2f}")
    print(f"The total price of the sales:     ${total_price:,.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
