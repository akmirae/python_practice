# 1.4 Use what you've learned about the binary numbering system to convert the following binary numbers to decimal.
binary_number = input("Enter a binary number: ")

if all(char in '01' for char in binary_number):
    decimal_number = int(binary_number, 2)
    print(f"The decimal number of '{binary_number}' is '{decimal_number}'.")
else:
    print("Invalid binary number. Please enter only 0s and 1s.")
