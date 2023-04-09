"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module"""
    def test_add_numbers(self):
        """ Test adding numbers"""
        res = calc.add(1,2)
        self.assertEqual(res, 3)

    def test_subtract(self):
        res = calc.subtract(7,4)
        self.assertEqual(res, 3)