"""Test the beamer.files module

Which should read property files in csv format
    And trees files in json format
"""

import random
from unittest import TestCase

import pytest

from beamer import files

class TestBeamerFiles(TestCase):
    """Test that beamer.files handles expected files OK

    These tests expect default data files to be
        1. present in project's root directory
        2. Correctly formatted

    And expect two default files to exist
        1. csv file with property data
        2. json file with trees data
    """
    pass


class TestFiles(TestBeamerFiles):
    """Test that beamer.files module handles property files"""

    def test_read_no_properties_path(self):
        """Test read_properties() with no path"""
        with pytest.raises(ValueError):
            _ = files.read_properties(None)

    def test_read_empty_properties_path(self):
        """Test read_properties() with empty path"""
        with pytest.raises(ValueError):
            _ = files.read_properties("")

    def test_read_properties(self):
        """Test read_properties() reads something from default properties file

        And the something is a list
        """
        properties = files.read_properties(files.default_properties_path)
        assert properties
        assert isinstance(properties, list)

    def test_read_properties_columns(self):
        """Test read_properties() recognises column names

        Take some random row after reading
            Treat it as a dict, expect column names to be the keys

        Some expected column names:
            'Address', 'Street Name', 'Price'
        """
        rows = files.read_properties(files.default_properties_path)
        assert len(rows)
        row = random.choice(rows)
        assert isinstance(row, dict)
        assert 'Address' in row
        assert 'Street Name' in row
        assert 'Price' in row


class TestTreesFiles(TestBeamerFiles):
    """Test that beamer.files module handles trees files"""

    def test_read_no_trees_path(self):
        """Test read_trees() with no path"""
        with pytest.raises(ValueError):
            _ = files.read_trees(None)

    def test_read_empty_trees_path(self):
        """Test read_trees() with empty path"""
        with pytest.raises(ValueError):
            _ = files.read_trees("")

    def test_read_trees(self):
        """Test read_trees() reads something from default trees file

        And the something is a dict
        """
        trees = files.read_trees(files.default_trees_path)
        assert trees
        assert isinstance(trees, dict)

    def test_read_trees_dict(self):
        """Test read_trees() recognises top level of expected dict

        Some expected key names:
            'short', 'tall'

        data can be arbitrary below the top-level
            so that's as far down as we go
        """
        trees = files.read_trees(files.default_trees_path)
        assert 'short' in trees
        assert 'tall' in trees


class TestParseTrees(TestTreesFiles):
    """Test that beamer.files module parses trees correctly"""

    def test_parse_trees(self):
        """Test parse_trees() returns two sets"""
        trees = files.read_trees(files.default_trees_path)
        short, tall = files.parse_trees(trees)
        assert isinstance(short, set)
        assert isinstance(tall, set)

    def test_known_short_tall_streets(self):
        """Test parse_trees() recognises known trees

        "clearwater" is known to be in the "short" section of defaualt trees file
        "adelaide road" is known to be in the "tall" section of defaualt trees file
        """
        trees = files.read_trees(files.default_trees_path)
        short, tall = files.parse_trees(trees)
        assert "clearwater" in short
        assert "adelaide road" in tall
