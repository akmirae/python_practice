# Write a program that uses nested loops to draw this pattern:
# *******
# ******
# *****
# ****
# ***
# **
# *

rows = 7
for star in range (rows, 0, -1):
    print("*" * star)