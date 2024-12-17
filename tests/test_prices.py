"""Test beamer.prices

Test edge cases for beamer.prices
"""

from unittest import TestCase

import pytest

from beamer.prices import convert_price_to_float
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
