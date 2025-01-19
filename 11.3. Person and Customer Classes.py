# 11.3. Person and Customer Classes
# Write a class named Person with data attributes for a person's name, address, and
# telephone number. Next, write a class named Customer that is a subclass of the
# Person class. The Customer class should have a data attribute for a customer number,
# and a Boolean data attribute indicating whether the customer wishes to be on a mailing
# list. Demonstrate an instance of the Customer class in a simple program.

class Person():
    def __init__(self, name, address, telephone):
        self.__name = name
        self.__address = address
        self.__telephone = telephone
        
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
        
    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address
    
    def get_telephone(self):
        return self.__telephone
    def set_telephone(self, telephone):
        self.__telephone = telephone
        
        
class Customer(Person):
    def __init__(self, name, address, telephone, customer_number, on_mailing_list):
        super().__init__(name, address, telephone)
        self.__customer_number = customer_number
        self.__on_mailing_list = on_mailing_list
        
    def get_customer_number(self):
        return self.__customer_number
    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number
        
    def get_on_mailing_list(self):
        return self.__on_mailing_list
    def set_on_mailing_list(self, on_mailing_list):
        self.__on_mailing_list = on_mailing_list

def main():
        
    name = input("Enter the customer's name: ")
    address = input("Enter the customer's address: ")
    telephone = input("Enter the customer's phone number: ")
    customer_number = input("Enter the customer number: ")
    on_mailing_list = input("Is the customer on the mailing list?(yes/no): ")
    
    on_mailing_list = on_mailing_list.lower() == 'yes'
    
    customer = Customer(name, address, telephone, customer_number, on_mailing_list)
    
    print("\nCustomer Details:")
    print('==========================')
    print(f"Customer's Name: {customer.get_name()}")
    print(f"Customer's Address: {customer.get_address()}")
    print(f"Customer's Telephone: {customer.get_telephone()}")
    print(f"Customer number: {customer.get_customer_number()}")
    print(f"Is the customer on the mailling list? {'Yes' if customer.get_on_mailing_list() else 'No'}")
if __name__ == '__main__':
    main()    