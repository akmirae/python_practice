# 3.8 Hot Dog Cookout Calculator
# Assume hot dogs come in package of 10, and hot dog buns come in package of 8. 
# Write a program that calculates the number of packages of hot dogs and the 
# number of packages of hot dog buns needed for a cookout, with the minimum amount 
# of leftovers. The program should ask the user for the number of people attending 
# the cookout and the number of hot dogs each person will be given. 
# The program should display the following details: 
#  * The minimum number of packages of hot dogs required
#  * The minimum number of packages of hot dog burns required
#  * The number of hot dogs that will be left over
#  * The number of hot dog buns that will be left over
import math

# Set the fixed variables.
DOGS_PACK = 10 # How many hot dogs in a package of hot dogs.
BUNS_PACK = 8  # How many hot dog buns int a package.

# Ask the user to input the number of people attending and hot dogs each person will be given.
try:
    people = int(input("Enter the number of people attending: "))
    hotdogs_per_person = int(input("Enter the number of hot dogs per person will be given: "))

    if people < 1 or hotdogs_per_person < 1:
        print("Error: people and hotdogs per person cannot be less than 1.")
    else:
        # Calculate and display the result.
        total_serves = people * hotdogs_per_person # Total serves for the people.
        pack_dogs = math.ceil(total_serves/DOGS_PACK) # The number of the packages of hot dogs needed.
        pack_burns = math.ceil(total_serves/BUNS_PACK) # The number of the packages of buns needed.
        leftover_dogs = pack_dogs * DOGS_PACK - total_serves # The number of leftover of hot dogs
        leftover_buns = pack_burns * BUNS_PACK - total_serves # The number of leftover of buns.
    
        print("\n               ***** Hot Dog Cookout Calculator *****")
        print("="*70)
        print(f"{'The minimum number of packages of hot dogs required':<55} {pack_dogs:10}")
        print(f"{'The minimum number of packages of hot dog buns required':<55} {pack_burns:10}")
        print(f"{'The number of hot dogs that will be left over':<55} {leftover_dogs:10}")
        print(f"{'The number of hot dog buns that will be lert over':<55} {leftover_buns:10}")
    
except ValueError:
    print("Invalid input. Please enter positive values for people and hotdogs per person.")
    