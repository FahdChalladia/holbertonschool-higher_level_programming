#!/usr/bin/python3
"""Defines a class Square with property access to size."""


class Square:
    """Class that defines a square with size validation."""

    def __init__(self, size=0):
        """Initialize a new square with optional size."""
        self.size = size  # Use setter here

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the square's size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
