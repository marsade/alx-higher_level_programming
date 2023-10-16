#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

    def test_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        

if __name__ == '__main__':
    unittest.main()