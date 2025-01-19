# 3.5 Mass and Weight
# Scientists measure an object's mass in kilograms and its weight in newtons. if you 
# know the amount of mass of an object in kilograms, you can calculate its weight in 
# newtons with the following formula:
# weight = mass x 9.8

# Write a program that asks the user to enter an object's mass, then calculates its weight.
# If the object weights more than 500 newtons, display a message indicating that is is too 
# heavy. If the object weights less than 100 newtons, display a message indicating that 
# it is too light.

try:
    # Ask the user to input a Mass.
    mass = float(input("Enter an object's mass in kilograms: "))
    
    # Calculate the weight and display the result with  messages for some weights.
    weight = mass * 9.8
    if weight < 0:
        print("\nError: The mass cannot be negative values.")
    elif weight < 100:
        print(f"\nThe weight '{weight:,.2f}' newtons are too light.")
    elif weight <= 500:
        print(f"\nThe weight is '{weight:,.2f}' newtons. It is within the acceptable range.")
    else:
        print(f"\nThe weight '{weight:,.2f}' newtons are too heavy.")
        
except ValueError:
    print("Invalid Input. Please enter a positive integer for the mass.")