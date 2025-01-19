# 6.7. Random Number File Writer
# Write a program that writes a series of random numbers to a file. Each random number
# should be in the range of 1 through 500. The application should let the user specify
# how many random numbers the file will hold.

import random

def write_random_numbers_to_file(filename, count):
    try:
        with open(filename, 'w') as file:
            for _ in range(count):
                random_number = random.randint(1, 500)
                file.write(f"{random_number}\n")
        print(f"Successfully wrote {count} random numbers to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    filename = input("Enter the file name to save random numbers (e.g., random_numbers.txt): ")
    count = int(input("Enter how many random numbers to generate: "))
    
    if count <= 0:
        print("The count must be a positive integer.")
    else:
        write_random_numbers_to_file(filename, count)
except ValueError:
    print("Invalid input. Please enter a valid number.")
        