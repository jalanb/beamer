"""Provides a command line interface to beamer"""

import os
import sys

from beamer import files
from beamer import prices


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
    try:
        short_average, tall_average, currency = script(
            files.default_properties_path, files.default_trees_path
        )
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
