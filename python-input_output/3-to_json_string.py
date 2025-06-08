#!/usr/bin/python3
"""
This module provides a function that returns the JSON repr of a Python obj.
"""


import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON string."""
    return json.dumps(my_obj)
