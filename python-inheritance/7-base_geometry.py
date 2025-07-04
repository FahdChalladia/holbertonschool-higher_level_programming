#!/usr/bin/python3
"""
This module defines the BaseGeometry class with validation.
"""


class BaseGeometry:
    """Base class for geometry with validation methods."""

    def area(self):
        """Raises an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer and greater than 0.
        Raises TypeError or ValueError with appropriate messages.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
