# 2.11 Lion and Tiger Percentages
# Write a program that asks the user for the number of lions and the number of tigers in the
# Big Cat exhibit at the local zoo. The program should display the percentage of lions
# and tigers in the exhibit.

try:
    lions = int(input("Enter the number of lions: "))
    tigers = int(input("Enter the number of tigers: "))
    total_cats = lions + tigers
    
    if lions < 0 or tigers <0 or total_cats == 0:
        print("Error: The number of lions and tigers cannot be negative or the number of the Big Cat should be positive integer")
    else:
        rate_lions = lions / total_cats * 100
        rate_tigers = tigers / total_cats * 100
        print("\n**** Lion and Tiger Percentages in the Big Cat exhibit ****")
        print("=" * 60)
        print(f"{'The Percentages of Lion':<30} {rate_lions:>10,.2f}%")
        print(f"{'The percentages of Tiger':<30} {rate_tigers:>10,.2f}%")
        
except ValueError:
    print("Invalid Input. Please enter positive integers for the number of lions and tigers.")
        