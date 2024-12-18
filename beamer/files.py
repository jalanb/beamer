"""Read files for beamer package

Should be able to read *.csv and *.json files
"""

import csv
import json
from pathlib import Path

# Known encodings for data files we have seen
known_encodings = ["utf-8", "windows-1252"]

# We expect default files in root directory of project
_project_root = Path(__file__).parent.parent
default_properties_path = _project_root / "dublin-property.csv"
default_trees_path = _project_root / "dublin-trees.json"


def read_properties(path_to_properties: str) -> list:
    """Read a csv file with property data at that path

    Return a list of rows from the file
    """
    if not path_to_properties:
        raise ValueError(f"Empty path to csv file: {path_to_properties!r}")
    for encoding in known_encodings:
        try:
            with open(path_to_properties, encoding=encoding) as stream:
                return list(csv.DictReader(stream))
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Bad encoding in file: {path_to_properties!r}")


def read_trees(path_to_json: str) -> dict:
    """Read a json file with trees data at given path

    Return a dict with the file's data
    """
    if not path_to_json:
        raise ValueError(f"Empty path to json file: {path_to_json!r}")
    for encoding in known_encodings:
        try:
            with open(path_to_json, encoding=encoding) as stream:
                return json.load(stream)
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Bad encoding in file: {path_to_json!r}")
