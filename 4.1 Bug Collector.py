# 4.1 Bug Collector
# A bug collector collects bugs every day for five days. Write a program that keeps 
# a running total of the number of bugs collected during the five days. The loop 
# should ask for the number of bugs collected for each day, and when the loop is 
# finished, the program should display the total number of bugs collected.

# Initialize the total number of bugs collected

total_bugs = 0

# Loop for 5 days.
for day in range(1,6):
    # Ask the user to enter the number of bugs collected for each day
    bugs_collected = int(input(f"Enter the number of bugs of day {day}: "))
    
    # Add the daily count to the total.
    total_bugs += bugs_collected
    
# Display the total number of bugs collected
print(f"The total number of bugs collected over 5 days is: {total_bugs}.")
