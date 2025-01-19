# 2.8 Tip, Tax and Total
# Write a program that calculates the total amount of a meal purchase at a restaurant.
# The program should ask the user to enter the charge for the food, then calculate the amounts of a
# 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
tip = 0.18
sales_tax = 0.07

try:
    meal_purchase = float(input("Enter the total amount of your meal purchase: "))
    
    
    if meal_purchase < 0:
        
        print("Error: The amount of your meal purchase cannot be negative. Please enter a positive number. ")
    else:
        tip_amount = tip * meal_purchase
        tax_amount = sales_tax * meal_purchase
        total_amount = meal_purchase + tip_amount + tax_amount
        
        print("\n**** Tip, Tax and Total Amount ****")
        print("=" * 40)
        print(f"{'Purchase Amount':<20} ${meal_purchase:>10,.2f}")
        print(f"{'Tip Amount':<20} ${tip_amount:>10,.2f}")
        print(f"{'Sales Tax Amount':<20} ${tax_amount:>10,.2f}")
        print("-"*40)
        print(f"{'Total Amount':<20} ${total_amount:>10,.2f}")
        
except ValueError:
    print("Invalid input. Please enter a numeric value for meal purchase amount.")