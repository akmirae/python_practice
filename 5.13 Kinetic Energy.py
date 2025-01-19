# 5.13 Kinetic Energy
# In physics, an object that is in motion is said to have kinetic energy. The following
# formula can be used to determine a moving object's kinetic energy:

# KE = 1/2 m * (v**2)

# The variables in the formula are as follows: KE is the kinetic energy, m is the object's
# mass in kilograms, and v is the object's velocity in meters per second.

# Write function named kinetic_energy that accepts an object's mass (in kilograms)
# and velocity (in meters per second) as arguments. The function should return the amount 
# of kinetic energy that the object has. Write a program that asks the user to enter
# values for mass and velocity, then calls the Kinetic_energy function to get the
# object's kinetic energy.

# Function to calculate kinetic energy

# Function to calculate kinetic energy
def kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

# Main program
# Ask the user for mass and velocity
mass = float(input("Enter an object's mass (in kilograms): "))
velocity = float(input("Enter the object's velocity (in meters per second): "))

# Calculate kinetic energy by calling the function
ke = kinetic_energy(mass, velocity)

# Display the result
print(f"\nThe kinetic energy is {ke:,.2f} J.")
