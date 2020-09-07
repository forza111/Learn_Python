import Bigger_price
import unittest

class test_bigger_price(unittest.TestCase):
    def test_price(self):
        self.assertEqual(Bigger_price.bigger_price((2,([{'name':'kakawka', 'price':30},
        {'name':'zalypa','price':10},{'name':'sychara','price':20
        }])),[{'name':'kakawka', 'price':30}, {'name':'sychara','price':20}]))