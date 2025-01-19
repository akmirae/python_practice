# 7.3. Rainfall Statistics
# Design a program that lets the user enter the total rainfall for each of 12 months 
# into a list. The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, the months with the highest and lowest amounts.

def rainfall_statistics():
    # List to store rainfall data for 12 months
    rainfalls = []
    
    # Loop to collect rainfall data
    for month in range(1, 13):  # Loop through 1 to 12
        while True:  # Loop until a valid input is provided
            try:
                monthly_rainfall = float(input(f"Enter the rainfall for month {month}: "))
                if monthly_rainfall < 0:  # Ensure the input is non-negative
                    print("Rainfall cannot be negative. Please try again.")
                    continue
                rainfalls.append(monthly_rainfall)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    
    # Calculate total, average, highest, and lowest rainfall
    total_rainfall = sum(rainfalls)
    average_rainfall = total_rainfall / 12
    highest_rainfall = max(rainfalls)
    lowest_rainfall = min(rainfalls)
    
    # Find the months with highest and lowest rainfall
    highest_month = rainfalls.index(highest_rainfall) + 1
    lowest_month = rainfalls.index(lowest_rainfall) + 1
    
    # Display results
    print(f"\nTotal rainfall for the year: {total_rainfall:.2f}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Month with highest rainfall: Month {highest_month} ({highest_rainfall:.2f})")
    print(f"Month with lowest rainfall: Month {lowest_month} ({lowest_rainfall:.2f})")

# Call the function
rainfall_statistics()
