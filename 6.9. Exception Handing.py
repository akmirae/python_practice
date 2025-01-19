# 6.9. Exception Handing
# Modify the program that you wrote for Exercise 6.6 so it handles the following
# exceptions:
# It should handle any IOError exceptions that are raised when the file is
# opened and data is read from it.
# It should handle any ValueError exceptions that are raised when the items
# that are read from the file are converted to a number.

def calculate_average_with_exceptions(filename):
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            total = 0
            count = 0
            for line in file:
                try:
                    number = int(line.strip())  # Convert line to an integer
                    total += number
                    count += 1
                except ValueError:
                    # Handle invalid data in the file
                    print(f"Skipping invalid line: {line.strip()}")
            
            if count == 0:
                print("The file is empty or contains no valid numbers.")
            else:
                average = total / count
                print(f"\nThe average of numbers from the file: {average:,.2f}")
    
    except FileNotFoundError:
        # Handle file not found error
        print("Error: The file does not exist. Please check the filename and path.")
    except IOError:
        # Handle other I/O errors
        print("Error: An I/O error occurred while accessing the file.")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")

# Example usage:
filename = 'D:/Dong Kim/CCC/2024/20242Fall/Python/numbers.txt'
calculate_average_with_exceptions(filename)
 
