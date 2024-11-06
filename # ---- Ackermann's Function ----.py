# ---- Ackermann's Function ----
# Ackermann's Function is a recursive mathematical algorithm that can be
# used to test how well a system optimizes its performance of recursion.
# Design a function ackermann(m,n), which solves Ackermann's function. 
# Use the following logic in your function:

# If m = 0 then return n + 1
# If n = 0 then return ackermann(m -1,  1)
# Otherwise, return ackermann(m - 1, ackermann(m, n - 1))

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
    
print(ackermann(1 , 2))