#!/usr/bin/python3
"""Defines a Rect class with print_symbol and instance count track."""


class Rectangle:
    """Defines a rect with width, height, print symbol."""

    number_of_instances = 0
    print_symbol = "#"  # Default symbol

    def __init__(self, width=0, height=0):
        """Initialize the rectangle, validate width/height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter with type and value checks."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return string representation."""
        if self.__width == 0 or self.__height == 0:
            return ""
        # Use str() on print_symbol to handle any type
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return string representation to recreate the object via eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message on deletion and decrement instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
