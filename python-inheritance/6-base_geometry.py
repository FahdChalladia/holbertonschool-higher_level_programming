#!/usr/bin/python3
"""
This module defines the BaseGeometry class with an area method.
"""


class BaseGeometry:
    """Base class for geometry that defines common interface."""

    def area(self):
        """exception indicating that the area method is not implemented."""
        raise Exception("area() is not implemented")
