import unittest
from app.routes import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3,4,5]
        result = sum(data)
        self.assertEqual(result, 15)
    
    def test_list_float(self):
        data = [1.2, 0.5, 1.3, 3.2]
        result = sum(data)
        self.assertEqual(result, 1.2+0.5+1.3+3.2)
    def test_list_with_negative_value(self):
        data = [1, 2, 3, 4, -5]
        result = sum(data)
        self.assertEqual(result, 5)
    def test_with_tupple(self):
        data = (1, 2, 3, 4, 5)
        result = sum(data)
        self.assertEqual(result, 15)
    def test_with_string(self):
        data = ['1','2',3,4,5]
        result = sum(data)
        self.assertEqual(result,15)
    def test_negative_input(self):
        data = [-1, 2, 3, 4]
        result = sum(data)
        self.assertEqual(result, 8 )
    def test_no_value(self):
        data = []
        result = sum(data)
        self.assertEqual(result, 0)
    def test_no_num(self):
        data = ['i dont know']
        result = sum(data)
        self.assertEqual(result, 15)
        
  
