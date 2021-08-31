import unittest
from iq_test import iq_test

class Test(unittest.TestCase):
    def test_iq_test(self):
        self.assertEqual(iq_test("2 4 7 8 10"),3)
        self.assertEqual(iq_test("1 2 2"),1)

if __name__ == '__main__':
    unittest.main()
    print("iq_test: [Ok]")