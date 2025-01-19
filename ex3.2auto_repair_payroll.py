# ex3.2auto_repair_payroll
# Chris owns an auto repair business.
# If any employee works over 40 hours in a week, they are paid 1.5 times their regular hourly 
# pay rate for all hours over 40.  We need to calculate an employee's gross pay, including 
# any overtime wages. 

# Set the base hours and overtime rate.
BASE_HOURS = 40
OT_RATE = 1.5

# Ask an user to input data(employee's name, hours worked, hourly pay rate)

try:
    name = input("Enter an employee's name: ")
    hours_worked = float(input("Enter the hours worked: "))
    pay_rate = float(input("Enter the hourly pay rate: "))

    # calculate the gross pay.
    if hours_worked <= 40:
        gross_pay = hours_worked * pay_rate
        print(f"\n{name}'s gross pay is ${gross_pay:,.2f}.")
    else:
        gross_pay_ot = BASE_HOURS * pay_rate + (hours_worked - BASE_HOURS) * pay_rate *OT_RATE
        print(f"\n{name}'s gross pay is ${gross_pay_ot:,.2f}.")
        
except ValueError:
    print("Invalid input. Please enter positive valuse for hours worked and pay rate.")
