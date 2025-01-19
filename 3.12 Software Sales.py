# 3.12 Software Sales
# A software company sells a package that retails for $99. Quantity discounts are 
# given according to the following table:
#           Quantity            Discount
#           10-19                   10%
#           20-49                   20%
#           50-99                   30%
#           100 or more             40%

# Write a program that asks the user to enter the number of packages purchased. 
# The program should then display the amount of the discount(if any) and 
# the total amount of the purchase after the discount.

# Define the constant.
PACKAGE_PRICE = 99.00

def calculate_total_cost():
    
    # When the user enter letters but numbers, display error messages.(try:... except)
    try:
        # Ask the user to enter the number of packages purchased.
        num_packages = int(input("enter the number of packages purchased:"))    
    
        # Check for invalid input
        if num_packages < 0:
            print("Error: The number of packages purchased cannot be negative value.")
        # Calculate the discount rate based on the quantity
        elif num_packages < 10:
            discount_rate = 0
        elif num_packages < 20:
            discount_rate = 0.1
        elif num_packages < 50:
            discount_rate = 0.2
        elif num_packages < 100:
            discount_rate = 0.3
        else:
            discount_rate = 0.4
        
        # Calculate the total amount before and after the discount
        total_amount = PACKAGE_PRICE * num_packages
        discount_amount = total_amount * discount_rate        
        total_after_discount = total_amount - discount_amount
        # Display the results
        print(f"\n{'Total before discount':<30} ${total_amount:>10,.2f}")
        if discount_rate > 0:
            print(f"{'Discount applied':<30} ${discount_amount:>10,.2f}")
        print(f"{'Total after discount':<30} ${total_after_discount:>10,.2f}")
    except ValueError:
        print('Invalid Input. Please enter zero or a positive value for the number of packages purchased.')
# Run the function
calculate_total_cost()    
        