from citi import citi_country
import unittest

class proverka(unittest.TestCase):
    def test_citycountry(self):
        name = citi_country('santiago','chili',23)
        self.assertEqual(name,'Santiago, Chili, 23')