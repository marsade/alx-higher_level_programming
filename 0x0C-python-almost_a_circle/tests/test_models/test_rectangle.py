#!/usr/bin/python3
"""Unittests for Rectangle class"""
from models.base import Base
from models.rectangle import Rectangle
import unittest


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
    
    def test_exceptions(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = -20
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            r2 = Rectangle(10, 2)
            r2.x = {}
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

if __name__ == '__main__':
    unittest.main()