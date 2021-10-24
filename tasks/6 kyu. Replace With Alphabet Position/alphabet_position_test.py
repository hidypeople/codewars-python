import unittest
from alphabet_position import alphabet_position

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(
            alphabet_position("The sunset sets at twelve o' clock."),
            "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")

if __name__ == '__main__':
    unittest.main()
    print("persistence: [Ok]")