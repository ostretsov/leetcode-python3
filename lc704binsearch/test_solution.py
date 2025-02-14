from unittest import TestCase

from lc704binsearch.solution import Solution


class TestSolution(TestCase):
    def test_search(self):
        s = Solution()
        # self.assertEqual(0, s.search([-1,0,3,5,9,12], -1))
        self.assertEqual(1, s.search([-1,0,3,5,9,12], 0))
        # self.assertEqual(2, s.search([-1,0,3,5,9,12], 3))
        # self.assertEqual(3, s.search([-1,0,3,5,9,12], 5))
        # self.assertEqual(4, s.search([-1,0,3,5,9,12], 9))
        # self.assertEqual(5, s.search([-1,0,3,5,9,12], 12))
        # self.assertEqual(-1, s.search([-1,0,3,5,9,12], 13))
