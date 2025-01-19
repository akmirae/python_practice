# 6.6. Average of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the
# computer’s disk. Write a program that calculates the average of all the numbers stored
# in the file.

def calculate_average_from_file(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            count = 0
            
            for line in file:
                # Strip whitespace and ensure the line is not empty
                stripped_line = line.strip()
                if stripped_line.isdigit():  # Check if the line contains numeric data
                    number = int(stripped_line)
                    total += number
                    count += 1
            
            if count == 0:
                print("The file is empty or contains no valid numbers.")
            else:
                average = total / count
                print(f"\nThe average of numbers from the file: {average:,.2f}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains invalid data that could not be processed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the file path
filename = "D:/Dong Kim/CCC/2024/20242Fall/Python/numbers.txt"

# Call the function
calculate_average_from_file(filename)
       
            