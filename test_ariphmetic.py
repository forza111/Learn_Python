from ariphm import matematica
import unittest

class proverka(unittest.TestCase):
    def test_posmotrim(self):
        name = matematica(10,5,'/')
        self.assertEqual(name,2)
a = {1:123,2:12313}
print(a.get(2))






if __name__ == '__name__':
    unittest.main()
