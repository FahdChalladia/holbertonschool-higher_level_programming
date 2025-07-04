#!/usr/bin/python3
"""
This module defines the inherits_from function,
which checks if an object is a subclass a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
