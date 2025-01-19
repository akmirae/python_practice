# 2.1 Personal Information
# write a program that displays the following information for a student:
# * Name
# * Address, with city, state, and ZIP
# * Telephone number
# # College major

name = input("Enter a Student Name: ")
address = input("Enter the Student's Address (street number, city, state, zip): ")
telephone = input("Enter the Student's Telephoe Number: ")
college_major = input("Enter the Student's Major: ")

print("\n Student Personal Information")
print('=================================')
print(f"Name: {name}")
print(f"address: {address}")
print(f"Telephone: {telephone}")
print(f"College Major: {college_major}")
