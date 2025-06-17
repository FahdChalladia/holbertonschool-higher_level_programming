#!/usr/bin/python3
"""Def a funct that returns the list of available attri & methods of an obj."""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
