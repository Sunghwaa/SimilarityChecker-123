from unittest import TestCase

from length_checker import LengthChecker


class TestLengthChecker(TestCase):
    def test_length_score_when_length_is_twice(self):
        self.checker = LengthChecker()
        self.assertEqual(0, self.checker.check("A", "BB"))
