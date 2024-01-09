#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Parameters:
    - obj: Any object

    Returns:
    - List of strings representing attributes and methods
    """
    return [attr for attr in dir(obj)]
