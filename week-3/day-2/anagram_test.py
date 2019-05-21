from anagram_work import anagram
import unittest

class anagram_test(unittest.TestCase):
    def test_anagram(self, s1 = "god", s2 = "dog"): 
        
        self.assertTrue(anagram(s1, s2))

if __name__ == "__main__":
    unittest.main()
