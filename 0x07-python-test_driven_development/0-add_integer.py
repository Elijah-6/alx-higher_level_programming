#!/usr/bin/python3
"""Defines a function that adds two integers or floats
"""

def add_integer(a, b=98):
    """Add two integers.

    Args:
        a (int): integer to add.
        b (int): second integer to add.
    
    Raises:
        TypeError: if a or b are not integers or floats

    Returns:
        int: result of adding a and b.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))