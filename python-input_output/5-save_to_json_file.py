#!/usr/bin/python3
"""
This module provides a function to write a Py object to a file in JSON format.
"""

import json


def save_to_json_file(my_obj, filename):
    """Writes a Python object to a file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
