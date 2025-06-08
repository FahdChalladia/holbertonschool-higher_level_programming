#!/usr/bin/python3
"""
test
"""


def append_write(filename="", text=""):
    """ test """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
