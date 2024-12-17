"""Handle prices for beamer

We expect prices to look like this in data files:
    € 23,456.78

Need to convert that to floats for use in calculations

>>> from beamer.prices import convert_price_to_float as cpf

>>> assert cpf("€ 23,456.78") == 23_456.78
"""

import re


class BadPriceFormat(Exception):
    """Exception for bad price format"""

    pass


class UnknownCurrencyError(BadPriceFormat):
    """Exception for unknown currency"""

    pass


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
    known_currencies = "$£€"
    stripped = re.sub(f"[, {known_currencies}]", "", price).strip()
    try:
        return float(stripped)
    except ValueError:
        try:
            # Quick check if there is a bad currency symbol at the start of string
            no_currency = stripped[1:]
            _ = float(no_currency)
            raise UnknownCurrencyError(price)
        except ValueError:
            pass
        raise BadPriceFormat(f"Bad price: {price!r}") from None
