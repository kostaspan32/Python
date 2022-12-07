import unittest
from assert_test import su

class MySumTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(su([1, 2, 3]), 6)

    def test_2(self):
        self.assertEqual(su(), 0)