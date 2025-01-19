# 4.10 Tuition Increase
# At one college, the tuition for a full-time student is $8,000 per semester. It has 
# been announced that the tuition will increase by 3 percent each year for the next 
# 5 years. Write a program with a loop that displays the projected semester tuition 
# amount for the next 5 years.


print("\nYear      Tuition / Semester")
print("-" * 30)

# Initial tuition fee
tuition = 8000

# Loop through the next 5 years
for year in range(1, 6):  # Start from year 1
    tuition = tuition * 1.03  # Increase tuition by 3%
    print(f"{year:<10} ${tuition:,.2f}")

print("-" * 30)
