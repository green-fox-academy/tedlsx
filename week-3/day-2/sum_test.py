from sum_work import math_sum
import unittest

class sum_test(unittest.TestCase):
    def test_sum_empty(self, my_list = []):
        s = math_sum(my_list)
        self.assertEqual(s.sum(), sum(my_list))
    def test_sum_multiple(self, my_list = [1,2,3,4,5]):
        s = math_sum(my_list)
        self.assertEqual(s.sum(), sum(my_list))
    def test_sum_single(self, my_list = [1]):
        s = math_sum(my_list)
        self.assertEqual(s.sum(), sum(my_list))
    def test_sum_none(self, my_list = None):
        s = math_sum(my_list)
        self.assertEqual(s.sum(), sum(my_list))
if __name__ == "__main__":
    unittest.main()