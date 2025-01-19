# 6.1 File Display

# Assume a file containing a series of integers is named numbers.txt and exists on the
# computer’s disk. Write a program that displays all of the numbers in the file.

def display_numbers_from_file():
    try:
        # Open the file in read mode
        with open("numbers.txt", "r") as file:
            print("Numbers in the file:")
            for line in file:
                # Strip any extra whitespace and print the number
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'numbers.txt' does not exist.")
    except ValueError:
        print("Error: The file contains invalid data.")

# Call the function
display_numbers_from_file()
