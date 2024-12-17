"""Read files for beamer package

Should be able to read *.csv and *.json files
"""

import csv
import json


def read_csv_file(path_to_csv: str) -> list:
    """Read a csv file at that path

    Return a list of rows from the file
    """
    if not path_to_csv:
        raise ValueError(f"Empty path to csv file: {path_to_csv!r}")
    with open(path_to_csv, encoding="windows-1252", errors="replace") as stream:
        return list(csv.DictReader(stream))


def read_json_file(path_to_json: str) -> dict:
    """Read a json file at given path

    Return:
        Content of json file, as dict
    """
    if not path_to_json:
        raise ValueError(f"Empty path to json file: {path_to_json!r}")
    with open(path_to_json, encoding="utf-8", errors="replace") as stream:
        return json.load(stream)
