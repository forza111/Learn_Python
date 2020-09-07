import full_name
import unittest

#class abracadabra(unittest.TestCase):
    #def test_full_nam1111e(self):
        #self.assertEqual(full_name.full_name('Nikita','Ionkin','Alekseevich'),'Nikita Ionkin Alekseevich')



class TestUM(unittest.TestCase):
    def tearDownClass(cls):
        pass
        print('GAVNO')

    def tearDown(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual(3 * 4, 12)

    def test_strings_a_3(self):
        self.assertEqual('a' * 3, 'aaa')


if __name__ == '__main__':
    unittest.main()