#!/usr/bin/python3
"""
0-add_integer module
Contains a function to add two integers or floats with type validation.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to int).

    Args:
        a (int or float): first number
        b (int or float, optional): second number, defaults to 98

    Raises:
        TypeError: if a or b is not int or float

    Returns:
        int: sum of a and b casted to int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
