# ---- Sum of Numbers ----
# Design a function that accepts an integer argument and returns the sum of 
# all the integers from 1 up to the number passed as an argument.
# For example, if 50 is passed as an argument, the function will return the sum
# of 1,2,3,4,... 50. Use recursion to calculate the sum.
def sum_num(n):
    if n == 1:
        return 1
    else:
        return n + sum_num(n-1)
    
print(sum_num(50))