# ex3.4grader
# This program gets a numeric test score from the user and displays the corresponding letter grade
# Named constants to represent the grade.
A_score = 90
B_score = 80
C_score = 70
D_score = 60

# Get a test score from the user.
score = int(input("Enter your test score: "))

# Grade the score.
if score >= A_score:
    print("Your grade is A.")
else:
    if score >= B_score:
        print("Your grade is B.")
    else:
        if score >= C_score:
            print("Your grade is C.")
        else:
            if score >= D_score:
                print("Your grade is D.")
            else:
                print("Your score is F.") 