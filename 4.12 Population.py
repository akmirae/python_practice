# 4.12 Population
# Write a program that predicts the approximate size of a population of organisms. 
# The application should prompt the user to enter the starting number of organisms, 
# the average daily population increase (as a percentage), and the number of days 
# the organisms will be left to multiply. For example, assume the user enters 
# the following values:

# Starting number of organisms: 2
# Average daily increase: 30%
# Number of days to multiply: 10
# The program should display the following table of data:

#       Day         Approximate Population
#   ----------------------------------------
#       1           2
#       2           2.6
#       3           3.38
#       4           4.394
#       5           5.7122
#       6           7.42586
#       7           9.653619
#       8           12.5497
#       9           16.31462
#       10          21.209

# Ask the user to input data
starting = int(input("Enter the starting number of organisms: "))
increase = float(input("Enter the average daily increase (%): "))
days = int(input("Enter the number of days to multiply: "))

# Display header
print("\nDay       Approximate Population")
print("-"*40)

for day in range(1, days + 1):
    if day == 1:
        population = starting
    else:    
        population *= (1 + increase / 100)
    print(f"{day:<10} {population:.6g}")
