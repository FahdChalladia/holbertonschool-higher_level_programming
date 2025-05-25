#!/usr/bin/python3
"""
This module contains the function text_indentation(text)
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.
    No spaces at the beginning or end of each printed line.

    Args:
        text (str): The text to indent.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    length = len(text)

    while i < length:
        char = text[i]
        result += char
        if char in ['.', '?', ':']:
            # Add two new lines after the punctuation
            result += "\n\n"
            # Skip all spaces after punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    # Print lines without leading/trailing spaces
    for line in result.splitlines():
        print(line.strip())
