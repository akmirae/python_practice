# ex3.5conditional_expression
# This program demonstrates a conditional  expression.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

max = num1 if num1 > num2 else num2

print(f"The bigger number is {max}.")