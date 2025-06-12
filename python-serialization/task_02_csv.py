#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into JSON format and saves it as 'data.json'.

    Parameters:
    - csv_filename (str): The path to the input CSV file.

    Returns:
    - True if conversion is successful.
    - False if an error occurs (e.g., file not found).
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
