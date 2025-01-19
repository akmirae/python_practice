# 5.10 Math Quiz
# Write a program that gives simple math quizzes. The program display two random
# numbers that are to be added, such as:
#   247
# + 129
#
# The program should allow the student to enter the answer. If the answer is correct,
# a message of congratulations should be displayed. If the answer is incorrect, 
# a message showing the correct answer should be displayed
import random

def math_quiz():
    # Generate two random numbers between 1 and 999
    num1 = random.randint(1, 999)
    num2 = random.randint(1, 999)
    
    # Display the problem
    print(f"\n  {num1}")
    print(f"+ {num2}")
    print("--------")
    
    # Get the user's answer
    user_answer = int(input("Enter your answer: "))
    
    # Calculate the correct answer
    correct_answer = num1 + num2
    
    # Check the user's answer and respond
    if user_answer == correct_answer:
        print("\nCongratulations! That's correct!")
    else:
        print(f"\nSorry, that's incorrect. The correct answer is {correct_answer}.")

# Run the quiz
math_quiz()

