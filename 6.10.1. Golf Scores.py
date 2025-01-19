# 6.10.1. Golf Scores
# The Springfork Amateur Golf Club has a tournament every weekend. The club
# president has asked you to write two programs:
# A program that will read each player’s name and golf score as keyboard input,
# then save these as records in a file named golf.txt. (Each record will have a
# field for the player’s name and a field for the player’s score.)
# A program that reads the records from the golf.txt file and displays them.

def save_golf_scores(filename):
    try:
        with open(filename, 'w') as file:
            print("Enter player names and scores. Type 'done' as the name to stop.")
            while True:
                name = input("Enter player's name: ").strip()
                if name.lower() == 'done':
                    break
                try:
                    score = int(input(f"Enter {name}'s score: "))
                    file.write(f"{name},{score}\n")
                except ValueError:
                    print("Invalid score. Please enter a numeric value.")
                    continue
        print(f"Scores have been saved to {filename}")
    except IOError:
        print("An error occurred while writing to the file.")

filename = 'D:/Dong Kim/CCC/2024/20242Fall/Python/golf.txt'

save_golf_scores(filename)