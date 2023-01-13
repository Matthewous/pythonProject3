import unittest

from main import name_by_doc

class TestFunction(unittest.TestCase):
    
    # Проверка на введение корректного номера
    def test_name_by_doc_correct(self):
        etalon = f'\nВладелец документа Аристарх Павлов\n-----------'
        result = name_by_doc(10006)
        self.assertEqual(etalon, result)
    
    # Проверка на введение некорректного номера
    def test_name_by_doc_incorrect(self):
        etalon = f"\nДокумент не найден\n-----------"
        result = name_by_doc(10006)
        self.assertEqual(etalon, result)

