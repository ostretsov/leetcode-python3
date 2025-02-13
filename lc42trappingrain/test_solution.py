from unittest import TestCase

from lc42trappingrain.solution import Solution


class TestSolution(TestCase):
    def test_trap(self):
        s = Solution()
        self.assertEqual(0, s.trap([0]))
        height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        self.assertEqual(6, s.trap(height))
        height.reverse()
        self.assertEqual(6, s.trap(height))

    def test_lake_size(self):
        s = Solution()
        self.assertEqual(1, s.lake_size([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 1, 3))
        self.assertEqual(4, s.lake_size([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 3, 7))
