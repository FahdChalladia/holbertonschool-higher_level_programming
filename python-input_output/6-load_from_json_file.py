#!/usr/bin/python3
"""
This module provides a function that loads a Py object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Reads a JSON file and returns the corresponding Python object."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
