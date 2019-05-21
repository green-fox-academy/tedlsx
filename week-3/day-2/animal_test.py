from animal_work import animal
import unittest

class animal_test(unittest.TestCase):
    def test_eat(self):
        s = animal()
        self.assertEqual(s.eat(), "hunger is 49")

    def test_drink(self):
        s = animal()
        self.assertEqual(s.drink(), "thirst is 49")

    def test_play(self):
        s = animal()
        self.assertEqual(s.play(), "hunger is 51, thirst is 51")

    
if __name__ == "__main__":
    unittest.main()