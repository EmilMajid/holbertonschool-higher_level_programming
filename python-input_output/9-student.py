#!/usr/bin/python3
"""Defines a Student class with JSON serialization capability."""


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

    def to_json(self):
        """Retrieves a dictionary representation of the Student instance.
        Returns:
            dict: A dictionary containing the student's attributes
        """
        return self.__dict__
