from unittest import TestCase

from length_checker import LengthChecker


class TestLengthChecker(TestCase):
    def setUp(self):
        super().setUp()
        self.checker = LengthChecker()

    def test_length_score_when_length_is_twice(self):
        self.assertEqual(0, self.checker.check("A", "BB"))

    def test_length_score_when_length_is_same(self):
        self.assertEqual(60, self.checker.check("ASD", "DSA"))

    def test_length_score_when_length_diff_is_smaller_than_twice(self):
        self.assertEqual(20, self.checker.check("AAABB", "BAA"))
