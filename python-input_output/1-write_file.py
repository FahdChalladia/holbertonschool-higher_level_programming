#!/usr/bin/python3
"""
test
"""


def write_file(filename="", text=""):
    """ test """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
