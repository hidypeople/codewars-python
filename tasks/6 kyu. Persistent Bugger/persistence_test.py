import unittest
from persistence import persistence

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)

if __name__ == '__main__':
    unittest.main()
    print("persistence: [Ok]")