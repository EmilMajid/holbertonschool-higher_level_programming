#!/usr/bin/env python3
"""
XML Serialization and Deserialization Module

This module provides functions to convert between Python dictionaries and XML format.
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The Python dictionary to serialize
        filename (str): The name of the XML file to create
    """
    try:
        # Create the root element
        root = ET.Element("data")
        
        # Add each dictionary item as a child element
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        # Create the ElementTree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        
    except Exception as e:
        print(f"An error occurred during serialization: {str(e)}")
        raise

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The name of the XML file to read

    Returns:
        dict: The deserialized Python dictionary
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()
        
        # Reconstruct the dictionary
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        raise
    except Exception as e:
        print(f"An error occurred during deserialization: {str(e)}")
        raise
