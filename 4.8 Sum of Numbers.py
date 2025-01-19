# 4.8 Sum of Numbers
# Write a program with a loop that asks the user to enter a series of positive numbers.
# The user should enter a negative number to signal the end of the series. After all the 
# positive numbers have been entered, the program should display their sum.

sum = 0 
while True:
    
    num = float(input("Enter a positive numbers (or a negative number to finish): "))
    
    if num >= 0:
        sum += num   
       
    else:
        break

print(f"The sum of the numbers: {sum:,.2f}")