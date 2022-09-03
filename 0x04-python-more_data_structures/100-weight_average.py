#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not my_list:
        return 0
    average = 0
    weight = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        weight += tup[1]
    return float(average / weight)
