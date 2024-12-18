"""Handle prices for beamer

We expect prices to look like this in data files:
    € 23,456.78

Need to convert that to floats for use in calculations

>>> from beamer.prices import convert_price_to_float as cpf

>>> assert cpf("€ 23,456.78") == 23_456.78
"""

import re
from typing import Callable


class BadPriceFormat(Exception):
    """Exception for bad price format"""

    pass


class UnknownCurrencyError(BadPriceFormat):
    """Exception for unknown currency"""

    pass


_known_currencies = "$£€"


def convert_price_to_float(price: str) -> float:
    """Convert price to float

    Strips any currency signs, commas, extra spaces from the string
    Convert the stripped string to a float and return that

    Raise an exception if the price is not in known format
        Raise a UnknownCurrencyError if price is bad because of currency symbol

    >>> assert convert_price_to_float("123.45") == 123.45
    >>> assert convert_price_to_float("$ 123.45 ") == 123.45
    >>> assert convert_price_to_float("€9,123.45") == 9123.45
    """
    if not price:
        raise BadPriceFormat(f"Empty price: {price!r}") from None
    stripped = re.sub(f"[, {_known_currencies}]", "", price).strip()
    try:
        return float(stripped)
    except ValueError:
        try:
            # Quick check if there is a bad currency symbol at the start of string
            no_currency = stripped[1:]
            _ = float(no_currency)
            # If we got here, there was a bad currency symbol
            # Otherwise it was a "normal" ValueError, from bad numbers, or ...
            raise UnknownCurrencyError(price)
        except ValueError:
            pass
        raise BadPriceFormat(f"Bad price: {price!r}") from None


def average_price(properties: list, included: Callable):
    """Get the average price of some properties in that list

    `included()` takes a street name and returns True if it should be included

    >>> test_properties = [
    ...     {"Street Name": "Short Street", "Price": "€  100.11"},
    ...     {"Street Name": "Long Street", "Price": "€  900.99"},
    ...     {"Street Name": "Short Street", "Price": "€  300.33"},
    ... ]
    >>> included = lambda x: x == "Short Street"
    >>> expected = 200.22
    >>> actual = average_price(test_properties, included)
    >>> assert actual == expected
    """
    total, count = 0.0, 0
    for property in properties:
        if included(property["Street Name"]):
            total += convert_price_to_float(property["Price"])
            count += 1
    return total / count


def first_currency(properties: list) -> str:
    """Get the first currency in the list of properties

    >>> test_properties = [
    ...     {"Street Name": "Short Street", "Price": "€  100.11"},
    ...     {"Street Name": "Long Street", "Price": "$ 900.99"},
    ...     {"Street Name": "Short Street", "Price": "£ 300.33"},
    ... ]
    >>> expected = "€"
    >>> actual = first_currency(test_properties)
    >>> assert actual == expected
    """
    # regexp to look for known currencies at staart of a string
    currency_regexp = re.compile(f"^[{re.escape(_known_currencies)}]")
    for property in properties:
        price = property["Price"].strip()
        match = currency_regexp.search(price)
        if match:
            return match.group(0)
    raise ValueError("No knonw currency found in any property")
