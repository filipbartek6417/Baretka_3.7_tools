import time
import math

PI = math.pi

def print_run_time(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        string = 'The program ran for ' + '{:.10f}'.format(end - start) + ' seconds.'
        print(string)
        return result
    return wrapper

def calculate_deviation_from_PI(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        string = 'The method has a deviation of ' + '{:.10f}'.format(abs(PI - result)) + '.'
        print(string)
        return result
    return wrapper