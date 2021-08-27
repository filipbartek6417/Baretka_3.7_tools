# Disclaimer: The comments below are just my observations
# Do not consider them as verified justifications for respective algorithm's efficiency

import math
from baretka_prt import print_run_time

# Quite slow even at small numbers

@print_run_time
def explicit_pascal(n):
    n -= 1  # These things are just adjusting the fact that humans are stupid and count up from one and not zero
    return_list = []
    for i in range(n + 1):
        row = []
        for j in range(i + 1):
            row.append(int(math.factorial(i) / (math.factorial(i - j) * math.factorial(j))))
        # print(' '.join(map(str, row)))  # Turn on for printing the triangle on the fly
        return_list.append(row) # Turn on for storing a return list
    return return_list

# Only calculates a specified row of the triangle
# Quick, however, due to Python floating point arithmetic only able to compute up to approx. 1030
# After that, OverflowError

@print_run_time
def explicit_variable_pascal(n):
    n -= 1
    a = []
    for j in range(n + 1):
        a.append(int(math.factorial(n) / (math.factorial(n - j) * math.factorial(j))))
    return a

# As with all recursive algorithms, just don't use them if you work with larger datasets

# @print_run_time
def recursive_pascal(n):
    n -= 1
    return_list = []
    for i in range(n + 1):
        row = []
        for j in range(i + 1):
            row.append(recursive_pascal_yield(i, j))
        # print(' '.join(map(str, row)))
        return_list.append(row)
    return return_list

def recursive_pascal_yield(n, k):
    if k == 0 or k == n:
        return 1
    return recursive_pascal_yield(n - 1, k - 1) + recursive_pascal_yield(n - 1, k)

# This one is quite quick, however you will soon encounter memory error
# Could be maybe optimized by gradual shortening of the list, or implementing a data structure, e.g. linked list
# And keeping only the necessary parts for the next row

@print_run_time
def dynamic_pascal(n):
    n -= 1
    allRows = []
    for i in range(n + 1):
        allRows.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                allRows[i].append(1)
            else:
                allRows[i].append(allRows[i - 1][j - 1] + allRows[i - 1][j])
        # print(' '.join(map(str, allRows[i])))
    return allRows

# This one doesn't store the entire triangle
# However, it is quite quick for finding nth row of the triangle
# Avoids MemoryError

@print_run_time
def dynamic_variable_pascal(n):
    n -= 1
    a = []
    for i in range(n + 1):
        temp = []
        for j in range(i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(a[j - 1] + a[j])
        a = temp
        # print(a)  # Turn on if you want to print results on the fly
    return a