import unittest
from increment_string import increment_string

class Test(unittest.TestCase):
    def test_filter_list(self):
        self.assertEqual("1", increment_string(""))
        self.assertEqual("xxx1", increment_string("xxx"))
        self.assertEqual("foo1", increment_string("foo"))
        self.assertEqual("124", increment_string("123"))
        self.assertEqual("foo001", increment_string("foo000"))
        self.assertEqual("foo45", increment_string("foo44"))
        self.assertEqual("foo045", increment_string("foo044"))
        self.assertEqual("foo0012", increment_string("foo0011"))
        self.assertEqual("foo100", increment_string("foo099"))
        self.assertEqual("foo1000", increment_string("foo999"))
        self.assertEqual("xi7E1686454000000000677823", increment_string("xi7E1686454000000000677822"))

if __name__ == '__main__':
    unittest.main()
    print("find_it: [Ok]")