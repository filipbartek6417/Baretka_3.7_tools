import math

def recursive_fib(n):
    if n <= 2:
        return 1
    return recursive_fib(n - 1) + recursive_fib(n - 2)

def iterative_field_fib(n):
    field = [1,1]
    for i in range(2, n):
        field.append(field[i - 2] + field[i - 1])
    return field[-1]

def iterative_variable_fib(n):
    a, b = 1, 1
    for _ in range(2, n):
        temp = a
        a += b
        b = temp
    return a

def explicit_fib(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi ** n - (-1 / phi) ** n) / math.sqrt(5))
