# 6.5. Sum of Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the
# computer’s disk. Write a program that reads all of the numbers stored in the file and
# calculates their total.

def sum_of_numbers_in_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            total = 0
            # Iterate over each line, convert to integer, and add to the total
            for line in file:
                number = int(line.strip())  # Convert line to integer
                total += number
        
        # Display the total sum of numbers
        print(f"The total sum of numbers in the file '{filename}' is: {total}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric data.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the file name
filename = "D:/Dong Kim/CCC/2024/20242Fall/Python/numbers.txt"

# Call the function
sum_of_numbers_in_file(filename)


    
          
    
        