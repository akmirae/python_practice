# 6.8. Random Number File Reader
# This exercise assumes you have completed Programming Exercise 7, Random Number
# File Writer. Write another program that reads the random numbers from the file,
# displays the numbers, then displays the following data:
#  1. The total of the numbers
#  2. The number of random numbers read from the file

def sum_and_count_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            count = 0
            for line in file:
                stripped_line = line.strip()  # Use `line`, not `file`
                if stripped_line.isdigit():  # Check if it's a valid number
                    number = int(stripped_line)
                    total += number
                    count += 1
            
            if count == 0:
                print("The file is empty or contains no valid numbers.")
            else:
                print(f"\nThe sum of the numbers from the file: {total:,}")
                print(f"The total count of the numbers from the file: {count:,}")
    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and path.")
    except ValueError:
        print("Error: The file contains invalid data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
filename = "D:/Dong Kim/CCC/2024/20242Fall/Python/random_numbers.txt"
sum_and_count_numbers_from_file(filename)
