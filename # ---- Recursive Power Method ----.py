# ---- Recursive Power Method ----
# Design a function that uses recursion to raise a number to a power.
# The function should accept two arguments: the number to be raised,
# and the exponent. Assume the exponent is a nonnegative integer.
def recur_power(x, y):
    if y == 0 or x == 1:
        return 1
    else:
        return x * recur_power(x, y - 1)
    
print (recur_power(1, 1000000)) 