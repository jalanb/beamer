"""Read files for beamer package

Should be able to read *.csv and *.json files
"""

import csv
import json

# Known encodings for data files we have seen
known_encodings = ["utf-8", "windows-1252"]


def read_csv_file(path_to_csv: str) -> list:
    """Read a csv file at that path

    Return a list of rows from the file
    """
    if not path_to_csv:
        raise ValueError(f"Empty path to csv file: {path_to_csv!r}")
    for encoding in known_encodings:
        try:
            with open(path_to_csv, encoding=encoding) as stream:
                return list(csv.DictReader(stream))
        except UnicodeDecodeError:
            pass


def read_json_file(path_to_json: str) -> dict:
    """Read a json file at given path

    Return a dict with the file's data
    """
    if not path_to_json:
        raise ValueError(f"Empty path to json file: {path_to_json!r}")
    for encoding in known_encodings:
        try:
            with open(path_to_json, encoding=encoding) as stream:
                return json.load(stream)
        except UnicodeDecodeError:
            pass
