import math

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

def recursive_pascal_yield(n, k):
    if k == 0 or k == n:
        return 1
    return recursive_pascal_yield(n - 1, k - 1) + recursive_pascal_yield(n - 1, k)

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