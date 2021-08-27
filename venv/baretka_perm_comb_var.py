# Disclaimer: The comments below are just my observations
# Do not consider them as verified justifications for respective algorithm's efficiency

def permutations(n):
    return variations(n, len(n))

# All functions below have a predefined result length of 2, you can specify the length as an optional parameter

def combinations(n, k=2):
    return master_function(n, False, True, [], k)

def repeating_combinations(n, k=2):
    return master_function(n, True, True, [], k)

def variations(n, k=2):
    return master_function(n, False, False, [], k)

def repeating_variations(n, k=2):
    return master_function(n, True, False, [], k)

# Since all the algorithms behave similarly, it is possible by having 2 flags in the call
# to compute all of them by using a master function

def master_function(n, repeating, combination, return_list, k=2, current=''):
    if k == 0:
        # print(current)  # Turn this on if you want to print results as they come
        return_list.append(current)  # Turn this on if you want to store a return list
        return return_list
    for item in n:
        return_list = master_function(n if repeating else n.replace(item, "", 1), repeating, combination, return_list, k - 1, current + item)
        if combination: n = n[1:]
    return return_list