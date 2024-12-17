"""Check that an app is provided

Recognise an app as "module at top level that has a `main()` function"

"""

from unittest import TestCase

class MainTest(TestCase):
    def test_main(self):
        """Check that a __main__ module exists"""
        from beamer import __main__

    def test_main_has_main(self):
        """Check that a __main__ module has a `main()` function"""
        from beamer import __main__
        assert hasattr(__main__, 'main')
        main_method = __main__.main
        assert callable(main_method)
