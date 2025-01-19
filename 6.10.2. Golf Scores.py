# 6.10.2. Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club
# president has asked you to write two programs:
# A program that will read each player’s name and golf score as keyboard input,
# then save these as records in a file named golf.txt. (Each record will have a
# field for the player’s name and a field for the player’s score.)
# A program that reads the records from the golf.txt file and displays them.

def read_golf_scores(filename):
    try:
        with open(filename, 'r') as file:
            print("\nPlayer Scores:")
            print("-" * 20)
            for line in file:
                name, score = line.strip().split(',')
                print(f"Name: {name}, Score: {score}")
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print("An error occurred while reading the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Specify the full path to the file
filename = 'D:/Dong Kim/CCC/2024/20242Fall/Python/golf.txt'

# Read and display player scores
read_golf_scores(filename)
