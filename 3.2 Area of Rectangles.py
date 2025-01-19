# 3.2 Area of Rectangles
# The area of a rectangle is the rectangle's length times its width. Write a program 
# that asks for the length and width of two rectangles. The program should tell 
# the user which rectangle has the greater area, or if the areas are the same.

# Create the lengths and widths of rectangle_1 and rectangle_2.
length_1 = int(input("Enter the length of rectangle 1: "))
width_1 = int(input("Enter the width of rectangle 1: "))
length_2 = int(input("Enter the length of rectangle 2: "))
width_2 = int(input("Enter the width of rectangle 2: "))

# Compare the two rectangles.
area_1 = length_1 * width_1  # The area of rectangle 1
area_2 = length_2 * width_2  # The area of rectangle 2

print(f"\nThe area of the rectangle 1 is {area_1}.")
print(f"The area of the rectangle 2 is {area_2}.")
print("=" *50)
if area_1 > area_2:
    print("\nThe area of the rectangle 1 is greater than rectangle 2.")
elif area_1 == area_2:
    print("\nThe area of the rectangle 1 is the same as rectangle 2.")
else:
    print("\nThe area of the rectangle 2 is greater than rectangle 1.")
