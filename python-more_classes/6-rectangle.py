#!/usr/bin/python3
"""This module defines a Rectangle class with width and height attributes,
tracks number of instances, supports area, perimeter, string representation,
repr for eval, and prints a message when an instance is deleted.
"""


class Rectangle:
    """Defines a rectangle."""

    number_of_instances = 0  # Public class attribute tracking instances

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height (default 0)."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment on new instance

    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, validating type and value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, validating type and value."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter, or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string with '#' representing the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string that recreates the object with eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when a rec is deleted and decr instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
