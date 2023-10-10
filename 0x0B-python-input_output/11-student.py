#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize Student
        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary rep of student instance"""
        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""
        for k, v in json.items():
            setattr(self, k, v)
