# 4.11 Calculating the Factorial of a Number
# In mathematics, the notation n! represents the factorial of the nonnegative integer n.
# The factorial of n is the product of all the nonnegative integers from 1 to n. For Example,
#
# 7! = 1x2x3x4x5x6x7 =5,040

# and

# 4! = 1x2x3x4 = 24

# Write a program that lets the user enter a nonnegative integer then uses a loop to calculate
# the factorial of that number. Display the factorial.

factor = int(input("enter a nonnegative integer to calculate the factorial of that number: "))

# validate input
if factor < 0:
    print("Factorial is not defined for negative numbers.")
else: 
    # Initialize the result to 1 (factorial base case)   
    result_factoring = 1

    # Loop to calculate the factorial.
    for n in range(1, factor + 1):
        result_factoring *= n
    
    # Display the result
    print(f"{factor}! is {result_factoring}.")