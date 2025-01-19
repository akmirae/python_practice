# 20. Rock, Paper, Scissors Game
# Write a program that lets the user play the game of Rock, Paper, Scissors 
# against the computer. The program should work as follows:

# 1. When the program begins, a random number in the range of 1 through 3 is generated. 
#  If the number is 1, then the computer has chosen rock. If the number is 2, 
#  then the computer has chosen paper. If the number is 3, then the computer has chosen 
#  scissors. (Don’t display the computer’s choice yet.)
# 2. The user enters his or her choice of “rock,” “paper,” or “scissors” at the
#  keyboard.
# 3. The computer’s choice is displayed.
# 4. A winner is selected according to the following rules:
#    • If one player chooses rock and the other player chooses scissors, then rock
#      wins. (Rock smashes scissors.)
#    • If one player chooses scissors and the other player chooses paper, then
#      scissors wins. (Scissors cuts paper.)
#    • If one player chooses paper and the other player chooses rock, then paper
#      wins. (Paper wraps rock.)
#    • If both players make the same choice, the game must be played again to
#      determine the winner
# Be sure to divide the program into functions that perform each major task.

import random

def get_computer_choice():
    """Generate and return the computer's choice."""
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    return choices[random.randint(1, 3)]

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    """Main function to play the game."""
    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        # Get computer's choice
        computer_choice = get_computer_choice()

        # Get user's choice
        user_choice = input("\nEnter your choice (rock, paper, scissors): ").lower()

        # Validate user's input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        # Display computer's choice
        print(f"The computer chose: {computer_choice}")

        # Determine winner
        result = determine_winner(user_choice, computer_choice)

        if result == "tie":
            print("It's a tie! Play again.")
        elif result == "user":
            print("Congratulations! You win!")
            break
        else:
            print("Sorry, the computer wins!")
            break

# Run the game
play_game()
