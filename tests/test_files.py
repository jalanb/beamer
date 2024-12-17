"""Test the beamer.files module

Which should read given files in csv and json formats
"""

from pathlib import Path
from unittest import TestCase

import pytest

from beamer import files

# We expect default files in root directory of project
path_to_data = Path(files.__file__).parent.parent
default_csv_path = path_to_data / "dublin-property.csv"
default_json_path = path_to_data / "dublin-trees.json"

class TestFiles(TestCase):
    """Test the beamer.files module

    These tests expect daflt data files to be
        1. present in project's root directory
        2. Correctly formatted
    """

    def test_read_no_csv_path(self):
        """Test read_csv_file() with no path"""
        with pytest.raises(ValueError):
            _ = files.read_csv_file(None)

    def test_read_empty_csv_path(self):
        """Test read_csv_file() with empty path"""
        with pytest.raises(ValueError):
            _ = files.read_csv_file("")

    def test_read_no_json_path(self):
        """Test read_json_file() with no path"""
        with pytest.raises(ValueError):
            _ = files.read_json_file(None)

    def test_read_empty_json_path(self):
        """Test read_json_file() with empty path"""
        with pytest.raises(ValueError):
            _ = files.read_json_file("")

    def test_read_csv_file(self):
        """Test read_csv_file() reads something from default csv file

        And the something is a list
        """
        data = files.read_csv_file(default_csv_path)
        assert data
        assert isinstance(data, list)

    def test_read_json_file(self):
        """Test read_json_file() reads something from default json file

        And the something is a dict
        """
        data = files.read_json_file(default_json_path)
        assert data
        assert isinstance(data, dict)

    def test_read_csv_columns(self):
        """Test read_csv_file() recognises columns

        Some expected column names:
            'Address', 'Street Name', 'Price'
        """
        rows = files.read_csv_file(default_csv_path)
        assert len(rows)
        row = rows[0]
        assert isinstance(row, dict)
        assert 'Address' in row, row.keys()
        assert 'Street Name' in row, row.keys()
        assert 'Price' in row, row.keys()

    def test_read_json_dict(self):
        """Test read_json_file() recognises top level of expected dict

        Some expected key names:
            'short', 'tall'

        data can be arbitrary below the top-level
            so that's as far down as we go
        """
        data = files.read_json_file(default_json_path)
        assert 'short' in data
        assert 'tall' in data
