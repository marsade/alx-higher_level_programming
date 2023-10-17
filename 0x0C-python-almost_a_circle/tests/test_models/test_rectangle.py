#!/usr/bin/python3
"""Unittests for Rectangle class"""
from models.base import Base
from models.rectangle import Rectangle
import unittest
from unittest.mock import patch
import io


class RectangleTest(unittest.TestCase):
    """Test initialization of the Rectangle class"""
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


class TestRectangle_Area(unittest.TestCase):
    """test the results from the area method"""
    
    def test_area(self):
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)
        
    def test_area_one_arg(self):
        r = Rectangle(1, 3, 4, 5,)
        with self.assertRaises(TypeError):
            r.area(10)


class TestRectangle_Display(unittest.TestCase):
    """Test the display method of the rectangle."""
    def test_display(self):
        r1 = Rectangle(4, 6)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            rec_output = mock_stdout.getvalue()
        ex_output = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(rec_output, ex_output)

    def test_display_five_args(self):
        r1 = Rectangle(2, 2, 5, 6, 7)
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r1.display()
            rec_output = mock_stdout.getvalue()
        ex_output = "##\n##\n"
        self.assertEqual(rec_output, ex_output)

    def test_display_one_arg(self):
        r = Rectangle(2, 5, 6, 6)
        with self.assertRaises(TypeError):
            r.display(65, 7)
  
if __name__ == '__main__':
    unittest.main()