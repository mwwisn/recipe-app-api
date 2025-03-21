"""simple tests"""


from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    "test calculator module"
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract(self):
        "test substracting numbers"
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
