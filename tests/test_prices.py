"""Test beamer.prices

Test edge cases for beamer.prices
"""

from unittest import TestCase

import pytest

from beamer.prices import convert_price_to_float
from beamer.prices import first_currency
from beamer.prices import UnknownCurrencyError
from beamer.prices import BadPriceFormat

class TestPrices(TestCase):

    def test_missing_price(self):
        """Test missing price"""
        with pytest.raises(BadPriceFormat):
            convert_price_to_float(None)

    def test_empty_price(self):
        """Test missing price"""
        with pytest.raises(BadPriceFormat):
            convert_price_to_float("")

    def test_zero_prices(self):
        """Test missing price"""
        assert convert_price_to_float("0") == 0.0
        assert convert_price_to_float("0.00") == 0.0

    def test_known_currences(self):
        """Test that dollars, pounds and euros are handled"""
        expected = 123
        assert convert_price_to_float("$ 123") == expected
        assert convert_price_to_float("£ 123 ") == expected
        assert convert_price_to_float("€ 123") == expected

    def test_unknown_currencies(self):
        """Test some other currencies raise an exception

        This test is not comprehensive, just for coverage
            And lists of tested currencies may be changed in future
        """
        with pytest.raises(UnknownCurrencyError):
            convert_price_to_float("¥ 123")
        with pytest.raises(UnknownCurrencyError):
            convert_price_to_float("₴ 123 ")
        with pytest.raises(UnknownCurrencyError):
            convert_price_to_float("L 123 ")


class TestFirstCurrency(TestCase):
    """Check that first_currency() finds the first currency in a list of properties"""

    def first_currency_extracted(self):
        """Test that first currency is found"""
        properties = [
            {"Price": "$23.45"},
            {"Price": "£99.99"},
            {"Price": "543.21"},
        ]
        expected = "$"
        actual = first_currency(properties)
        assert actual == expected

    def test_no_properties_raises_error(self):
        """If no properties are given, an error is raised"""
        with pytest.raises(ValueError):
            first_currency([])

    def test_no_currencies_raises_error(self):
        """If properties are given, but none uses our currencies, an error is raised"""
        properties = [
            {"Price": "¥123.45"},
            {"Price": "999.99"},
            {"Price": "L 543.21"},
        ]
        with pytest.raises(ValueError):
            first_currency([])

    def test_bad_key_is_ignored(self):
        """If properties are given, but one excludes the expected "Price", that is ignored"""
        properties = [
            {"Price": "$23.45"},
            {"Bad Name": "£99.99"},
        ]
        with pytest.raises(ValueError):
            first_currency([])

    def test_bad_key_is_ignored(self):
        """If properties are given, but all exclude the expected "Price", that raises an error

        (effectively - same as no properties given (above)
        """
        properties = [
            {"Hello World": "$23.45"},
            {"Bad Name": "£99.99"},
        ]
        with pytest.raises(ValueError):
            first_currency([])
