# 1.5 Look at the ASCII chart in Appendex C and determine the codes for each letter
# of your first name.

first_name = input("Enter your first name: ")

print("ASCII codes for each letter in your name:")

for letter in first_name:
    print(f"{letter}: {ord(letter)}") # ord() function returns the ASCII code of a character.   