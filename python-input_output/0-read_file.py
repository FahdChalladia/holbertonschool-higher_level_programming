#!/usr/bin/python3
"""
This module provides a function to read&print the contents of a UTF-8 txt file.
"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
