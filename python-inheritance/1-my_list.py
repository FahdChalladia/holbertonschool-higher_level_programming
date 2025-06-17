#!/usr/bin/python3
"""This module defines a class MyList that inherits from the built-in list."""

class MyList(list):
    """A subclass of list with a method to print the list in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (does not modify the original list)."""
        print(sorted(self))
