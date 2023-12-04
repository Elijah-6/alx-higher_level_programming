#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = [x % 2 == 0 for x in my_list]
    return (multiples)
