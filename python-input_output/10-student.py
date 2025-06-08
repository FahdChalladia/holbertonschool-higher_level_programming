#!/usr/bin/python3
""" Student class with optional filtering in to_json """


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return dictionary representation of instance.
        If attrs is a list of strings, return only those attributes that exist.
        Otherwise return all attributes.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                attr: self.__dict__[attr]
                for attr in attrs if attr in self.__dict__
            }
        return self.__dict__.copy()
