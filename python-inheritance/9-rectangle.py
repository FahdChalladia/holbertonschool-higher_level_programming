#!/usr/bin/python3
"""
This module defines the Rectangle class with area and string representation.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class with area computation and formatted output."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
