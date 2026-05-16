import unittest

from src.calculations import sum , diff

class TestCalculations(unittest.TestCase):
    def Test_sum(self):
        res = sum( n1:10, n2:5 )
        self.assertEqual(res, second=15, msg='Addition Err')

    def Test_diff(self):
        res = diff( n1:10, n2:5 )
        self.assertEqual(res, second=15, msg='Subtraction Err')

    # def Test_mul(self):
    #     res = mul( n1:10, n2:5)
    #     self.assertEqual(res, second=15, msg='Multiplection Err')