from django.test import TestCase

class SomeTest(TestCase):
    """тест на токсичность"""

    def test_bad_maths(self):
        """тетс: неправильные математические расчеты"""
        self.assertEqual(1+1, 3)
