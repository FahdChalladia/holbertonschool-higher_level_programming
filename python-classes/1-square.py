#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""


class Square:
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square (no type/value checks yet).
        """
        self.__size = size
