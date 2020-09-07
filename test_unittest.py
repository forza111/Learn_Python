import unittest
from full_name import full_name
class NameTestCase(unittest.TestCase):
    '''Тесты для функции full_name.py'''
    def test_first_last_name(self):
        '''Имена вида Ионкин Никита работают нормально? '''
        '''Метод, начинающийся на "test_"  отрабатывают автоматически при исп-ии unittest '''
        format_name = full_name('Ионкин','Никита')
        self.assertEqual(format_name,'Ионкин Никита')
    def test_first_last_middle(self):
        format_name = full_name('Ионкин','Никита','Алексеевич')
        self.assertEqual(format_name,'Ионкин Никита Алексеевич')
if __name__ == '__name__':
    unittest.main()
