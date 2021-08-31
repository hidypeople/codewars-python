import unittest
from square_digits import square_digits

class Test(unittest.TestCase):
    def test_square_digits(self):
        self.assertEqual(square_digits(9119), 811181)
        self.assertEqual(square_digits(0), 0)


if __name__ == '__main__':
    unittest.main()
    print("square_digits: [Ok]")