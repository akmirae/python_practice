# 5.7 Paint Job Estimator
# A painting company has determined that for every 112 square feet of wall space,
# one gallon of paint and eight hours of labor will be required. The company charges
# $35.00 per hour for labor. Write a program that asks the user to enter the square
# feet of wall space to be painted and the price of the paint per gallon. The program
# should display the following data:
#  1. The number of gallons of paint required
#  2. The hours of labor required
#  3. The cost of the paint
#  4. The labor charges
#  5. The total cost of the paint job

import math

# Function to calculate the total cost of the paint job
def calculate_total_cost(costs):
    return sum(costs)

# Constants
COVERAGE_PER_GALLON = 112  # Square feet per gallon
HOURS_PER_GALLON = 8       # Labor hours per gallon
LABOR_COST_PER_HOUR = 35   # Labor cost per hour

# Input: Wall space and cost of paint per gallon
wall_space = float(input("Enter the wall space to be painted (in square feet): "))
cost_per_gallon = float(input("Enter the cost of the paint per gallon: $"))

# Calculations
gallons_required = math.ceil(wall_space / COVERAGE_PER_GALLON)
hours_required = gallons_required * HOURS_PER_GALLON
cost_of_paint = gallons_required * cost_per_gallon
labor_charges = hours_required * LABOR_COST_PER_HOUR
total_cost = calculate_total_cost([cost_of_paint, labor_charges])

# Output
print(f"\n1. The number of gallons of paint required: {gallons_required}")
print(f"2. The hours of labor required: {hours_required}")
print(f"3. The cost of the paint: ${cost_of_paint:,.2f}")
print(f"4. The labor charges: ${labor_charges:,.2f}")
print(f"5. The total cost of the paint job: ${total_cost:,.2f}")

