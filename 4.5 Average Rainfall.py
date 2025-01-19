# 4.5 Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years. The program should first ask for the number of years. 
# The outer loop will iterate once for each year. The inner loop will iterate twelve 
# times, once for each month.Each iteration of the inner loop will ask the user 
# for the inches of rainfall for that month. After all iterations, the program 
# should display the number of months, the total i nches of rainfall, 
# and the average rainfall per month for the entire period.

# Ask the user for the number of years.
years = int(input("Enter the period of years to collect data: "))
# Initialize the rainfall
total_rainfall = 0

# Outer loop: Iterate once for each year
for year in range(1, years +1):
    print(f"\nYear {year}:")
    # Inner loop: Iterate for 12 months
    for month in range(1, 13):
        # Ask the user to enter the inches of rainfall for the month.
        rainfall = float(input(f"The inches of rainfall for month {month}: "))
        total_rainfall += rainfall
        
# Calculate the total number of months        
total_months = years * 12

# Display the results
print(f"Total number of the month: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:,.2f} inches")
print(f"Average rainfall per month for the period: {total_rainfall / total_months:,.2f}")