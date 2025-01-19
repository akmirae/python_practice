# 5.5 Property Tax
# A county collects property taxes on the assessment value of property, which is 60
# percent of the property's actual value. For example, if an acre of land is valued at
# $10,000, its assessment value is $6,000. The property tax is then 72cents for each
# $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20.
# Write a program that asks for the actual value of a piece of property and displays 
# the assessment value and property tax.

# Function to calculate the property tax
def calculate_property_tax(assessment_value):
    return (assessment_value / 100) * 0.72

# Ask the user to enter the actual value of the property
actual_value = float(input("Enter the actual value of a piece of property: $"))

# Calculate the assessment value (60% of the actual value)
assessment_value = actual_value * 0.6

# Calculate the property tax
property_tax = calculate_property_tax(assessment_value)

# Display the results
print(f"\nAssessment value: ${assessment_value:,.2f}")
print(f"Property tax: ${property_tax:,.2f}")
