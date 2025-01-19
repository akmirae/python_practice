# 7.2. Lottery Number Generator
# Design a program that generates a seven-digit lottery number. The program should 
# generate seven random numbers, each in the range of 0 through 9, and assign 
# each number to a list element. (Random numbers were discussed in Chapter 5.) 
# Then write another loop that displays the contents of the list.

import random

def generate_lottery_number():
    # Create an empty list to hold the lottery numbers
    lottery_number = []
    
    # Generate 7 random numbers (0-9) and add them to the list
    for _ in range(7):
        number = random.randint(0, 9)  # Generate a random number between 0 and 9
        lottery_number.append(number)
    
    # Display the lottery number
    print("Your lottery number is:", end=" ")
    for num in lottery_number:
        print(num, end="")
    print()  # Newline for better output format

# Call the function
generate_lottery_number()

    
