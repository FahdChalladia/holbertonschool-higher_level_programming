#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Parameters:
    - dictionary (dict): The dictionary to serialize.
    - filename (str): The filename to save the XML data to.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except Exception:
        pass


def deserialize_from_xml(filename):
    """
    Deserializes XML content from a file into a dictionary.

    Parameters:
    - filename (str): The XML file to read from.

    Returns:
    - dict: A dictionary reconstructed from the XML data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {}
        for child in root:
            data[child.tag] = child.text
        return data
    except Exception:
        return None
