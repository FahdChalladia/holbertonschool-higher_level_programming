#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance to a file using pickle.

        Parameters:
        - filename (str): The path to the output pickle file.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            # Optionally, you could log the error
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object instance from a pickle file.

        Parameters:
        - filename (str): The path to the pickle file.

        Returns:
        - CustomObject instance or None if there's an error.
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                else:
                    return None
        except Exception:
            return None
