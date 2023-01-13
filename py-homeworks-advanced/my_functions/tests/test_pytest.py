import pytest

from main import name_by_doc

class TestFunction:
    
    # Проверка на введение корректного номера
    def test_name_by_doc_correct(self):
        etalon = f'\nВладелец документа Аристарх Павлов\n-----------'
        result = name_by_doc(10006)
        assert etalon == result
    
