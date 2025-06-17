#!/usr/bin/python3
"""Defines a Student class with selective JSON serialization capability."""


class Student:
    """Represents a student with basic information and JSON serialization."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list): Optional list of attribute names to include

        Returns:
            dict: A dictionary containing the requested student attributes
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
        for attr in attrs):
            return {key: value for key, value in self.__dict__.items() 
                    if key in attrs}
        return self.__dict__
