# 3.13 Shipping Charges
# The Fast Freight Shipping Company charges the following rates:

#   Weight of Package                           Rate per Pound
#   ===========================================================
#   2 pounds or less                                $1.50
#   Over 2 pounds but not more than 6 pounds        $3.00
#   Over 6 pounds but not more than 10 pounds       $4.00
#   Over 10 pounds                                  $4.75

# Write a program that asks the user to enter the weight of a package then displays 
# the shipping charges.

def calculate_shipping_charges():
    try:
        # When the user enter letters instead of numbers, display error messages.(try:... except)
        # Ask the user to enter the weight of a package.
        weight_package = float(input("Enter the weight of a package(use positive integers): "))
        
        # Display error message for negative input.
        if weight_package < 0:
            print("Error: The weight of package cannot be negative values.")
        # Calculate the shipping charges
        elif weight_package < 2:
            rate_per_pound = 1.50
        elif weight_package <= 6:
            rate_per_pound = 3.00
        elif weight_package <= 10:
            rate_per_pound = 4.00
        else:
            rate_per_pound = 4.75
        
        shipping_charge = weight_package * rate_per_pound
        print(f"Your shipping charge for {weight_package} pounds is ${shipping_charge:,.2f}.")
        
    except ValueError:
        print("Invalid Input. Please enter a numeric value for the weight of the package.")

# Run the function.
calculate_shipping_charges()