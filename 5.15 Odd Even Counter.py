# 5.15 Odd Even Counter
# In this chapter, you saw an example of how to write an algorithm that determines
# whether a number is even or odd. Write a program that generates 100 random numbers
# and keeps a count of how many of those random numbers are even, and how many of
# them are odd.

import random

def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

# Generate 100 random numbers between 1 and 100
random_numbers = [random.randint(1, 100) for _ in range(100)]

# Count even and odd numbers
even_count, odd_count = count_even_odd(random_numbers)

# Display the results
print(f"Out of 100 random numbers:")
print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")
