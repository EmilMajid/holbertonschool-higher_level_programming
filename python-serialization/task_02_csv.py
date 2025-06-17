#!/usr/bin/env python3
"""
CSV to JSON Conversion Module

This module provides a function to convert CSV data to JSON format and save it to a file.
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to convert

    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file and convert to list of dictionaries
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Serialize to JSON and write to file
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
