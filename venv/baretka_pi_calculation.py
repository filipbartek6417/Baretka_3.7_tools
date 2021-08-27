# Disclaimer: The comments below are just my observations
# Do not consider them as verified justifications for respective algorithm's efficiency

import math
import random
from baretka_prt import print_run_time, calculate_deviation_from_PI

PI = math.pi

# Implements the Gregory-Leibniz converging method for computing PI

@print_run_time
@calculate_deviation_from_PI
def gregory_leibniz(x=100000):
    n = 0
    for k in range(x):
        n += (-1) ** k / (2 * k + 1)
    return 4 * n

# Implements the Archimedes converging method for computing PI

@print_run_time
@calculate_deviation_from_PI
def archimedes_method(x=100000):
    a = 2 * math.sqrt(3)
    b = 3
    for i in range(x):
        a = (2 * a * b) / (a + b)
        b = math.sqrt(a * b)
    return a

# Monte Carlo algorithms: numerical methods based on random simulation

# Darts method chooses random points in a square with the side a = 1
# The area of a quarter-circle with the radius of 1 is PI / 4
# Therefore, the probability of a random point landing inside the quarter-circle is PI / 4
# This algorithm implements the fact to derive an approximation of the value of PI

@print_run_time
@calculate_deviation_from_PI
def darts_method(x=100000):
    approx = 4
    for i in range(x):
        x, y = random.random(), random.random()
        now_value = 4 * math.sqrt(x ** 2 + y ** 1)
        if abs(now_value - PI) < abs(approx - PI):
            approx = now_value
    return approx

# Buffon needle takes a segment of length l
# And repeatedly throws it on a sheet of paper with vertical lines spaced l units apart
# The probability of the thrown needle crossing one of the vertical lines is PI / 2
# This algorithm leverages from the fact to approximate the value of PI
# However, this program abstracts all the elements into one dimension for the sake of simplicity
# *Note the difference between probability of choosing a point on a line and on a circle
# in relation to the x-axis position of the point (it is an unfiorm distribution over 2 * PI)*

@print_run_time
@calculate_deviation_from_PI
def buffon_needle(x=100000):
    count = 0
    for _ in range(x):
        a = random.random() * 10
        b = a + math.cos(random.uniform(0, PI))
        if a // 1 != b // 1:
            count += 1
    return 2 / (count / x)
