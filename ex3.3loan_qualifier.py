# ex3.3loan_qualifier
# This program determines whether a bank customer qualifies for a loan

MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEAR = 2        # The minimum years on the job

# Get the customer's annual salary.
salary = float(input("Enter the annual salary: "))

# Get the number of years on the current job.
years = float(input("Enter the number of years on the current job: "))

# Determine whether the customer qualifies.
if salary >= MIN_SALARY:
    if years >= MIN_YEAR:
        print("The customer qualifies for the loan.")
    else:
        print(f"\nThe customer does not qualify for the loan. The customer must have been " 
            f"employed for at least {MIN_YEAR} years to qualify")
else:
    print(f"\nThe customer does not qualify for the loan.The customer must earn at least " 
        f"${MIN_SALARY:,.2f} per year to qualify")