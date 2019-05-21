from apple_work import apple

import unittest

class test_apple(unittest.TestCase):
    def test_apple_work(self):
        s = "apples"
        a = apple()
        self.assertEqual(a.get_apple(), s)

if __name__ == "__main__":
    unittest.main()