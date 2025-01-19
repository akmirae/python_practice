# 4.2 Calories Burned
# Running on a particular treadmill you burn 4.2 calories per minutes. Write a program 
# that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes

# Initialize the calories burned per minute.

burned_per_min = 4.2

print("\nMinutes      Calories burned")
print("=" * 30)

for min in range(10, 31, 5):
    calories = min * burned_per_min
    print(f"{min:<10} {calories:>10,}")
    
print("=" * 30)
     
    


















# calories_per_minute = 4.2

# # Loop for specific intervals: 10, 15, 20, 25, and 30 minutes
# for minutes in range(10, 31, 5):
#     # Calculate the calories burned
#     calories_burned = minutes * calories_per_minute
#     # Display the result
#     print(f"The calories after {minutes} minutes:  {calories_burned} calories.")
