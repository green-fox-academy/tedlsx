from count_work import count_str
import unittest

class count_c(unittest.TestCase):
    def test_count_str(self):
        s = "apple"
        self.assertEqual(count_str(s), {"a":1, "p":2, "l":1, "e":1})  

if __name__ == "__main__":
    unittest.main()