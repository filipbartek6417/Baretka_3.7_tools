import math
import random

PI = math.pi

def gregory_leibniz(x=100000):
    n = 0
    for k in range(x):
        n += (-1) ** k / (2 * k + 1)
    return 4 * n

def archimedes_method(x=100000):
    a = 2 * math.sqrt(3)
    b = 3
    for i in range(x):
        a = (2 * a * b) / (a + b)
        b = math.sqrt(a * b)
    return a

def monte_carlo(x=100000):
    approx = 4
    for i in range(x):
        x, y = random.random(), random.random()
        now_value = 4 * math.sqrt(x ** 2 + y ** 1)
        if abs(now_value - PI) < abs(approx - PI):
            approx = now_value
    return approx

def buffon_needle(x=100000):
    count = 0
    for _ in range(x):
        a = random.random() * 10
        b = a + math.cos(random.uniform(0, PI))
        if a // 1 != b // 1:
            count += 1
    return 2 / (count / x)
