#!/usr/bin/python3
"""
    Test Cases for Base class
"""
import os
import unittest
import json

from models.base import Base
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """ Unittests for Base class"""

    def setup(self):
        """Runs before each unit test"""
        Base._Base__nb_objects = 0

    def test_class_docstring(self):
        """ test doc string"""
        self.assertIsNotNone(Base.__doc__)

    def test_mult_bases(self):
        """test multiple cases"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_uniq_id(self):
        """test with uniq id"""
        self.assertEqual(22, Base(22).id)

    def test_none_id(self):
        """test with None as id"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 4)
        self.assertEqual(b2.id, 5)

    def test_public_id(self):
        """test public id"""
        b = Base(5)
        b.id = 10
        self.assertEqual(10, b.id)

    def test_to_json_type(self):
        """
            Testing the json string
        """
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        """
            Testing the json string
        """
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        """
            Testing the json string
        """
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        """
            Testing the json string
        """
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
