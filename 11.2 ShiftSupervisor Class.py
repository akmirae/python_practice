# 11.2 ShiftSupervisor Class
# In a particular factory, a shift supervisor is a salaried employee who supervises a shift.
# In addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets production
# goals. Write a ShiftSupervisor class that is a subclass of the Employee class your created in previous
# Exercise 1. The ShiftSupervisor class should keep a data attribute for the annual salary, and a data 
# attribute for the annual production bonus that a shift supervisor has earned. Demonstrate the class by 
# writing a program that uses a ShiftSupervisor object.

# ProductionWorker class, subclass of Employee
# Employee class



class Employee:
    def __init__(self, name, number):
        """Initialize Employee attributes."""
        self.__name = name
        self.__number = number

    # Accessor for name
    def get_name(self):
        return self.__name

    # Mutator for name
    def set_name(self, name):
        self.__name = name

    # Accessor for number
    def get_number(self):
        return self.__number

    # Mutator for number
    def set_number(self, number):
        self.__number = number


# ShiftSupervisor class (inherits from Employee)
class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, annual_bonus):
        """Initialize attributes from Employee and ShiftSupervisor."""
        super().__init__(name, number)  # Initialize Employee attributes
        self.__annual_salary = annual_salary  # Annual salary
        self.__annual_bonus = annual_bonus  # Annual production bonus

    # Accessor for annual salary
    def get_annual_salary(self):
        return self.__annual_salary

    # Mutator for annual salary
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    # Accessor for annual bonus
    def get_annual_bonus(self):
        return self.__annual_bonus

    # Mutator for annual bonus
    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus


# Main program
def main():
    # Prompt user for ShiftSupervisor data
    name = input("Enter the supervisor's name: ")
    number = input("Enter the supervisor's employee number: ")
    annual_salary = float(input("Enter the supervisor's annual salary: "))
    annual_bonus = float(input("Enter the supervisor's annual production bonus: "))

    # Create a ShiftSupervisor object
    supervisor = ShiftSupervisor(name, number, annual_salary, annual_bonus)

    # Display the supervisor's data
    print("\nShift Supervisor Details:")
    print(f"Name: {supervisor.get_name()}")
    print(f"Employee Number: {supervisor.get_number()}")
    print(f"Annual Salary: ${supervisor.get_annual_salary():,.2f}")
    print(f"Annual Production Bonus: ${supervisor.get_annual_bonus():,.2f}")


# Call the main function
if __name__ == "__main__":
    main()


