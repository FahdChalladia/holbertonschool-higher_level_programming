#!/usr/bin/python3
"""Defines a class Square that can print itself."""


class Square:
    """Class that defines a square with printable output."""

    def __init__(self, size=0):
        """Initialize the square with size."""
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
