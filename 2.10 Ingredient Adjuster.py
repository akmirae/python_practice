# 2.10 Ingredient Adjuster
# A cookie recipe calls for the following ingredients:
# * 1.5 cups of sugar
# * 1 cup of butter
# * 2.75 cups of flour
# The recipe produces 48 cookies with this amount of the ingredients. Write a program
# that asks the user how many cookies he or she wants to make, then displays the number
# of cups of each ingredient needed for the specified number of cookies.
sugar = 1.5
butter = 1
flour = 2.75
cookie_constant = 48

try:
    cookie_quantity = int(input("Enter the amount of cookies you want: "))
    sugar_amount = sugar / cookie_constant * cookie_quantity
    butter_amount = butter / cookie_constant * cookie_quantity
    flour_amount = flour / cookie_constant * cookie_quantity
    
    if cookie_quantity < 1:
        print("Error: Cookie quantity you want cannot be 0 or negative integers.")
    else:
        print("\n**** Ingredient Adjuster for Cookie ****")
        print("=" * 40)
        print(f"{'Cookie Quantity':<20} {cookie_quantity:>10}")
        print(f"{'Sugar':<20} {sugar_amount:>10,.2f} cups")
        print(f"{'Butter':<20} {butter_amount:>10,.2f} cups")
        print(f"{'Flour':<20} {flour_amount:>10,.2f} cups")
        
except ValueError:
    print("Invalid Input. Enter a positive integer for cookie quantity.")