# 4.7 Pennies for Pay
# Write a program that calculates the amount of money a person would earn over a period of 
# time if their salary is one penny the first day, two pennies the second day, and continues 
# to double each day. The program should ask the user for the number of days. Display a table 
# showing what the salary was for each day, then show the total pay at the end of the period. 
# The output should be displayed in a dollar amount, not the number of pennies.

days = int(input("Enter the number of days you worked: "))
total_salary = 0

print("Day                  Salary")
print("=" * 40)

for i in range(1,days + 1):
    salary = 2 ** (i-1)
    total_salary += salary
    print(f"{i:<20} ${salary / 100:,.2f}")
    
print("-" * 40)
print(f"Total Salary:        ${total_salary / 100:,.2f}")
    