#!/usr/bin/python3
"""MyList module."""

class MyList(list):
    """MyList inherits from list."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
