#!/usr/bin/env python3
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Parameters:
    - data (dict): The dictionary to serialize.
    - filename (str): The path to the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Parameters:
    - filename (str): The path to the input JSON file.

    Returns:
    - dict: The deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
