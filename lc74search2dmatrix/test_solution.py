from unittest import TestCase

from lc74search2dmatrix.solution import Solution


class TestSolution(TestCase):
    def test_search_matrix(self):
        s = Solution()
        self.assertTrue(s.searchMatrix([[1]], 1))
        self.assertTrue(s.searchMatrix([[1], [3]], 3))
        self.assertTrue(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
        self.assertTrue(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))
