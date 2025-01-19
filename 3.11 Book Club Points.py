# 3.11 Book Club Points
# Serendipity Booksellers has a book club that awards points to its customers based 
# on the number of books purchased each month. The points are awarded as follows:

# * If a customer purchases 0 books, he or she earns 0 points.
# * If a customer purchases 2 books, he or she earns 5 points.
# * If a customer purchases 4 books, he or she earns 15 points.
# * If a customer purchases 6 books, he or she earns 30 points.
# * If a customer purchases 8 or more books, he or she earns 60 points.

# Write a program that asks the user to enter the number of books that he or she has 
# purchased this month, then displays the number of points awarded.

try:
    # Ask the user to input the number of books that he or she has purchased this month.
    purchased = int(input("How many books have you purchase this month? "))
    
    # If the user input a negative value, display error message.
    if purchased < 0:
        print("Error: The number of this month purchased books cannot be negative value. ")
    elif purchased == 0:
        print("You awarded '0' Club Point.")
    elif purchased <= 2:
        print("You awarded '5' Club Point.")
    elif purchased <= 4:
        print("You awarded '15' Club Point.")
    elif purchased == 0:
        print("You awarded '0' Club Point.")
