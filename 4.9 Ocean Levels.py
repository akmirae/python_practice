# 4.9 Ocean Levels
# Assuming the ocean's level is currently rising at about 1.6 millimeters per year, 
# create an application that displays the number of millimeters that the ocean will 
# have risen each year for the next 25 years.

print("\nYear             Ocean Level(mm)")
print("="*40)

# Loop to calculate and display ocean level rise for the next 25 years
for year in range(0, 26):
    ocean_level = year * 1.6
    print(f"{year:<10} {ocean_level:>10,.1f}")    

print("="*40)    
