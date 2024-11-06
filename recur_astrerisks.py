# Write a recursive function that accepts an integer argument, n.
# The function should display n lines of asterisks on the screen,
# with the first line showing 1 asterisk, the second line showing 2 asterisks,
# up to the nth line which shows n asterisks.

def ast(n):
    if n == 1:
        print('*')
    else:
        ast(n-1)
        print('*' * n)
        
ast(6)