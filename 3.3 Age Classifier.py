# 3.3 Age Classifier
# Write a program that asks the user to enter a person's age. The program should display 
# a message indicating whether the person is an infant, a child, a teenager, or an adult.
# Following are the guidelines:
#  * If the person is 1 year old or less, they are an infant.
#  * If the person is older than 1 year, but younger than 13 years, they are a child.
#  * If the person is at least 13 years old, but less than 20 years old, they are a teenager.
#  * If the person is at least 20 years old, they are an adult.

# Ask the user to input the age.
try:
    age = int(input("Enter the age: "))
    
    # Categorize the age and show the result.
    if age < 0:
        print("Error: The age cannot be a negative value.")
    else:
        if age <= 1:
            print(f"{age} year old is classified as an infant.")
        elif age < 13:
            print(f"{age} years old is classified as a child.")
        elif age < 20:
            print(f"{age} years old is classified as a teenager.")
        else:
            print(f"{age} years old is classified as an adult")
except ValueError:
    print("Invalid Input. Please enter a positive integer for the age.")