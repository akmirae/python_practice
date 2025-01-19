# 1.3 Convert dicimal number to binary
number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    binary_representation = bin(number)[2:]
    print(f"The binary of '{number}' is '{binary_representation}'.")
        