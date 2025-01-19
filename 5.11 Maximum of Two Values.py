# 5.11 Maximum of Two Values
# Write a function named max that accepts two integer values as arguments and returns
# the value that is the greater of the two. For example, if 7 and 12 are passed as
# arguments to the function, the function should return 12. Use the function in a program
# that prompts the user to enter two integer values. The program should display the value
# that is the greater of the two.

# Function to find the maximum of two values
def max(value1, value2):
    if value1 > value2:
        return value1
    else:
        return value2

# Main program
# Prompt user for two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Call the max function and display the result
greater_value = max(num1, num2)
print(f"\nThe greater value is: {greater_value}")

