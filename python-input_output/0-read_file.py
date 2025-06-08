#!/usr/bin/python3
"""
This module provides a function to read and print the contents of a UTF-8 text file.
"""

def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
