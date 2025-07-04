#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize Square using Rectangle logic."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
