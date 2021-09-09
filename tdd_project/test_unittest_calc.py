import unittest
import calculator

class Calctest(unittest.TestCse):
    def test_add(self):
        self.assertEqual(calculator.add(2, 5), 7)
