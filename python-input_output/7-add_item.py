#!/usr/bin/python3
"""Script to add command-line arguments to a list and save to JSON file."""

import sys
from os import path
from typing import List

# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Main function to handle argument processing and file operations."""
    filename = "add_item.json"
    
    # Load existing list or create new one if file doesn't exist
    if path.exists(filename):
        items: List[str] = load_from_json_file(filename)
    else:
        items = []
    
    # Add all command-line arguments to the list
    items.extend(sys.argv[1:])
    
    # Save the updated list to the file
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
