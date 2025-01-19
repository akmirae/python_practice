# 6.4. Item Counter
# Assume a file containing a series of names (as strings) is named names.txt and
# exists on the computer’s disk. Write a program that displays the number of names that
# are stored in the file. (Hint: Open the file and read every string stored in it. Use a
# variable to keep a count of the number of items that are read from the file.)

def count_items(filename):
    try:
        with open(filename, "r") as file:
            count = 0
            for line in file:
                if line.strip():
                    count += 1
        print(f"\nThe file '{filename}' contains {count} names.")
        
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except ValueError:
        print("Error: The file contains invalid data.")
filename = 'D:/Dong Kim/CCC/2024/20242Fall/Python/names.txt'   
count_items(filename)
            