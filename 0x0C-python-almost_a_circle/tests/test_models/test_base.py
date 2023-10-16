#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.num1 = Base()
        self.num2 = Base(10)

    def test_init(self):
        self.assertEqual(self.num1.id, 1)
        self.assertEqual(self.num2.id, 10)
