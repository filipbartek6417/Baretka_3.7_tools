# Disclaimer: The comments below are just my observations
# Do not consider them as verified justifications for respective algorithm's efficiency

import math
from baretka_prt import print_run_time

# The worst algorithm, in both small and large cases (unsurprisingly)
# Don't use this please
# @print_run_time
def recursive_fib(n):
    return recursive_fib_yield(n)

def recursive_fib_yield(n):
    if n <= 2:
        return 1
    return recursive_fib_yield(n - 1) + recursive_fib_yield(n - 2)

# Quite quick for small numbers up to approx. 10000
# After that, you can expect at some point to encounter MemoryError (depends on your amount of RAM)
# (which will completely freeze your computer for a few minutes, don't recommend)
# However, may be useful if you need to store various members of the sequence

# @print_run_time
def iterative_field_fib(n):
    field = [1,1]
    for i in range(2, n):
        field.append(field[i - 2] + field[i - 1])
    return field[-1]

# A little bit slower than iterative field method
# However, you will definitely not encounter MemoryError
# And for PCs, this is the best option to get very large numbers in a reasonable time

# @print_run_time
def iterative_variable_fib(n):
    a, b = 1, 1
    for _ in range(2, n):
        temp = a
        a += b
        b = temp
    return a

# Best for both small and large numbers
# However, it requires storing large float numbers, which results in OverflowError
# Therefore its limits are equivalent to Python floating point precision
# It can probably be overcome by approximation of math.sqrt(5), but will ultimately result in incorrect results
# For truly large numbers however, it is still the fastest option, provided the floating point issues are solved

# @print_run_time
def explicit_fib(n):
    return int((((1 + math.sqrt(5)) / 2) ** n - (-1 / ((1 + math.sqrt(5)) / 2)) ** n) / math.sqrt(5))
