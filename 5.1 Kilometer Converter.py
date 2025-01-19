# 5.1 Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, then uses a function to convert 
# that distance to miles. The conversion formula is as follows:
# Miles = Kilometers X 0.6214

# Function to convert kilometers to miles
def convert_km_to_miles(kilometers):
    return kilometers * 0.6214

# Ask the user to enter the distance in kilometers
kilometers = float(input("Enter a distance in kilometers: "))

# Call the function to convert the distance
miles = convert_km_to_miles(kilometers)

# Display the result
print(f"{kilometers} km is {miles:,.2f} miles.")
