# 5.12 Falling Distance
# when an object is falling because of gravity, the following formula can be 
# used to determine the distance the object falls in a specific time period:
# d= 1/2 g t**2 
# The variables in the formula are as follows:
# • d is the distance in meters.
# • g is 9.8.
# • t is the amount of time, in seconds, that the object has been falling.
# Design a function named fallingDistance that accepts an object’s 
# falling time (in seconds) as an argument. The function should return the 
# distance, in meters, that the object has fallen during that time interval.
# Design a program that calls the function in a loop that passes the values 1 
# through 10 as arguments and displays the return value.

# Function to calculate falling distance
def fallingDistance(time):
    g = 9.8  # Acceleration due to gravity (m/s^2)
    distance = 0.5 * g * (time ** 2)
    return distance

# Main program
print("Time (s) | Distance (m)")
print("------------------------")
for t in range(1, 11):  # Loop through time values from 1 to 10 seconds
    distance = fallingDistance(t)
    print(f"{t:<8} | {distance:,.2f}")
