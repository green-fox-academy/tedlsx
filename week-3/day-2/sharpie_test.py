from sharpie_work import sharpie
import unittest

class sharpie_test(unittest.TestCase):
    def test_use(self):
        s = sharpie()
        s.use()
        self.assertEqual(s.ink_amount, 99)

if __name__ == "__main__":
    unittest.main()
