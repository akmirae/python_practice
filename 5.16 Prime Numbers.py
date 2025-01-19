# 5.16 Prime Numbers
# A prime number is a number that is only evenly divisible by itself and 1. 
# For example, the number 5 is prime because it can only be evenly by 1 and 5.
# The number 6, however, is not prime because it can be divided evenly 1,2,3 and 6.

# Write Boolean function named is_prime which takes an integer as an argument and
# returns true if the argument is a prime number, or false otherwise. Use the 
# function in a program that prompts the user to enter a number then displays a message
# indicating whether the number is prime.

# TIP: Recall that the % operator divides one number by another and returns the
# remainder of the division. In an expression such as num1 % num2, the %operator will
# return 0 if num1 is evenly divisible by num2.

# Function to check if a number is prime

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(number**0.5) + 1):  # Check divisors up to the square root of the number
        if number % i == 0:
            return False
    return True

# Prompt the user to enter a number
user_number = int(input("Enter a number to check if it's prime: "))

# Check if the number is prime and display the result
if is_prime(user_number):
    print(f"{user_number} is a prime number.")
else:
    print(f"{user_number} is not a prime number.")
