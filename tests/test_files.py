"""Test the beamer.files module

Which should read given files in csv and json formats
"""

from unittest import TestCase

import pytest

from beamer import files

class TestFiles(TestCase):
    """Test the beamer.files module

    These tests expect daflt data files to be
        1. present in project's root directory
        2. Correctly formatted
    """

    def test_read_no_csv_path(self):
        """Test read_properties() with no path"""
        with pytest.raises(ValueError):
            _ = files.read_properties(None)

    def test_read_empty_csv_path(self):
        """Test read_properties() with empty path"""
        with pytest.raises(ValueError):
            _ = files.read_properties("")

    def test_read_no_json_path(self):
        """Test read_trees() with no path"""
        with pytest.raises(ValueError):
            _ = files.read_trees(None)

    def test_read_empty_json_path(self):
        """Test read_trees() with empty path"""
        with pytest.raises(ValueError):
            _ = files.read_trees("")

    def test_read_properties(self):
        """Test read_properties() reads something from default csv file

        And the something is a list
        """
        properties = files.read_properties(files.default_properties_path)
        assert properties
        assert isinstance(properties, list)

    def test_read_trees(self):
        """Test read_trees() reads something from default json file

        And the something is a dict
        """
        trees = files.read_trees(files.default_trees_path)
        assert trees
        assert isinstance(trees, dict)

    def test_read_csv_columns(self):
        """Test read_properties() recognises columns

        Some expected column names:
            'Address', 'Street Name', 'Price'
        """
        rows = files.read_properties(files.default_properties_path)
        assert len(rows)
        row = rows[0]
        assert isinstance(row, dict)
        assert 'Address' in row
        assert 'Street Name' in row
        assert 'Price' in row

    def test_read_json_dict(self):
        """Test read_trees() recognises top level of expected dict

        Some expected key names:
            'short', 'tall'

        data can be arbitrary below the top-level
            so that's as far down as we go
        """
        trees = files.read_trees(files.default_trees_path)
        assert 'short' in trees
        assert 'tall' in trees
