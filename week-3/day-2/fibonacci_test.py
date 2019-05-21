from fibonacci_work import fi
import unittest

class fi_test(unittest.TestCase):
    def test_fi(self):
        my_list = [0, 1, 1, 2, 3, 5 ,8, 13, 21, 34, 55, 89]
        self.assertEqual(fi(), my_list)

if __name__ == "__main__":
    unittest.main()