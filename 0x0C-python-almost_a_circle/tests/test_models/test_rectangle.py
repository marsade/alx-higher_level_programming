#!/usr/bin/python3
"""Unittests for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    def test_init(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(4, 5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 7, 8, 9, 10)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 10)

    def test_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_isstance(self):
        self.assertIsInstance(Rectangle(1, 9), Base)

if __name__ == '__main__':
    unittest.main()