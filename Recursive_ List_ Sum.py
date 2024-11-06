# ---- Recursive List Sum ----
# Design a function that accepts a list of numbers as an argument.
# The function should recursively calculate the sum of all the numbers
# in the list and return that value.
def lst_sum(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 0:
        return 0
    else:
        return lst[0] + lst_sum(lst[1:])
    
numbers = [ 1, 8]    
print(lst_sum(numbers))
    