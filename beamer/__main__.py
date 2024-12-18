"""Provides a command line interface to beamer"""

import argparse
import os
import sys

from beamer import files
from beamer import prices


def parse_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Calculate average prices for short and tall trees",
    )
    parser.add_argument(
        "-p",
        "--properties",
        type=str,
        default=files.default_properties_path,
        help=f"Path to properties file (default: {files.default_properties_path})",
    )
    parser.add_argument(
        "-t",
        "--trees",
        type=str,
        default=files.default_trees_path,
        help=f"Path to trees file (default: {files.default_trees_path})",
    )
    return parser.parse_args()


def show_error(error: Exception) -> None:
    """Print error message to standard error"""
    print(str(error), file=sys.stderr)


def script(path_to_properties: str, path_to_trees: str) -> tuple[float, float, str]:
    """Read and process properties and trees data"""
    trees = files.read_trees(path_to_trees)
    short, tall = files.parse_trees(trees)
    properties = files.read_properties(path_to_properties)
    short_average = prices.average_price(properties, lambda x: x in short)
    tall_average = prices.average_price(properties, lambda x: x in tall)
    currency = prices.first_currency(properties)
    return short_average, tall_average, currency


def main() -> int:
    """Run beamer as a command line app

    This method only handles CLI arguments and errors
        And calls the script() function, above, for "the real work"
    """
    args = parse_args()
    try:
        short_average, tall_average, currency = script(args.properties, args.trees)
        print(f"Price average among short trees: {currency} {short_average:,.2f}")
        print(f"Price average among  tall trees: {currency} {tall_average:,.2f}")
    except ValueError as error:
        show_error(error)
        return os.EX_DATAERR
    except FileNotFoundError as error:
        show_error(error)
        return os.EX_OSFILE
    except Exception as error:
        show_error(error)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
