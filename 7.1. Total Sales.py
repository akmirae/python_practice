# 7.1. Total Sales
# Design a program that asks the user to enter a store’s sales for each day 
# of the week. The amounts should be stored in a list. Use a loop to calculate 
# the total sales for the week and display the result.

def total_sales():
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    sales =[]
    
    for day in days:
        while True:
            try:
                sale = float(input(f"Enter the sales for {day}: $"))
                if sale < 0:
                    print("Sales amount cannot be negative. Please enter a valid amount.")
                else:
                    sales.append(sale)
                    break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
                
    total = sum(sales)
    print(f"\nThe total sales for the week is: ${total:,.2f}")
    
total_sales()

            