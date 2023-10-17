#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    def test_init(self):
        num1 = Base()
        num2 = Base()
        num3 = Base(10)
        self.assertEqual(num1.id, num2.id - 1)
        self.assertEqual(num3.id, 10)

if __name__ == '__main__':
    unittest.main()