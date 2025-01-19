# 2.5 Distance Traveled
# Assuming there are no accidents or delays, the distance that a car travels down the interstate 
# can be calculated with the following formula:
# Distance = Speed X Time
# A car is traveling at 70 miles per hour. Write a program that displays the following:
# The user will input a travel time (hours).

speed = 70
travel_time = float(input("Enter the travel time(hours):"))
distance = travel_time * speed

if travel_time < 0:
    print("The travel time cannot be negative. Please enter a valid time.")
else:
    print(f"The travel distance for {travel_time} hours: {distance:,.2f} miles")