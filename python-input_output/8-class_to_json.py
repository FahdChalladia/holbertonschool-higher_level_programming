#!/usr/bin/python3
"""
Funct that return the dict desc for JSON serialization of an obj
"""


def class_to_json(obj):
    """Return the dict description of an object for JSON serialization."""
    return obj.__dict__
