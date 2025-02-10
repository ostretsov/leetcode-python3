from unittest import TestCase
from lc167twopointers.two_sum_2 import Solution


class TestSolution(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_twoSum(self):
        # self.assertEquals(self.solution.twoSum([2,7,11,15], 9), [1,2])
        # self.assertEquals(self.solution.twoSum([2,3,4], 6), [1,3])
        self.assertEquals(self.solution.twoSum([-1,0], -1), [1,2])

    def test_twoSum_ht(self):
        self.assertEquals(self.solution.twoSumOnePassHashTable([2,7,11,15], 9), [1,2])
        self.assertEquals(self.solution.twoSumOnePassHashTable([2,3,4], 6), [1,3])
        self.assertEquals(self.solution.twoSumOnePassHashTable([-1,0], -1), [1,2])
