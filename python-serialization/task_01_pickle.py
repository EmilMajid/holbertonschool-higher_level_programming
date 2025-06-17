#!/usr/bin/env python3
import pickle

class CustomObject:
    """A custom Python object that can be serialized using the pickle module.
    
    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        is_student (bool): Whether the person is a student
    """
    
    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.
        
        Args:
            name (str): The name to assign
            age (int): The age to assign
            is_student (bool): The student status to assign
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """Display the object's attributes in a formatted way.
        
        Prints:
            The object's name, age and student status in a human-readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")


    def serialize(self, filename):
        """Serialize the object to a file using pickle.
        
        Args:
            filename (str): The path of the file to save to
            
        Returns:
            None: Returns None if serialization fails
            
        Note:
            Uses binary write mode ('wb') for pickle compatibility
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")
            return None


    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject from a file.
        
        Args:
            filename (str): The path of the file to load from
            
        Returns:
            CustomObject: The deserialized object, or None if deserialization fails
            
        Note:
            Uses binary read mode ('rb') for pickle compatibility
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
