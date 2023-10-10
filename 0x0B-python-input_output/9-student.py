#!/usr/bin/python3
"""Student to JSON"""


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

    def to_json(self):
        """retrieves dictionary rep of student instance"""
        return self.__dict__
