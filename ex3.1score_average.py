# This program gets three test scores and displays their average. It congratulates 
# the user if the average is a high score.
# The HIGH_SCORE named constant holds the value that is considered a high score.

HIGH_SCORE = 95

# Get the 3 test scores.
test1 = int(input("Enter the 1st test score: "))
test2 = int(input("Enter the 2nd test score: "))
test3 = int(input("Enter the 3re test score: "))

# Calculate the averate for 3 test scores.
average = (test1 + test2 +test3) / 3

if average >= HIGH_SCORE:
    print(f"\nCongratulations!, Your Average is {average:,.2f}. You got high score.")
else:
    print(f"\nYour average score is {average:,.2f}")