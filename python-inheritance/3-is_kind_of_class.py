#!/usr/bin/python3
"""
This module defines the function is_kind_of_class,
which checks if an object is an instance of a class.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class."""
    return isinstance(obj, a_class)
