from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ri = len(matrix) - 1
        while ri >= 0 and matrix[ri][0] > target:
            ri -= 1

        row = matrix[ri]

        lft, rgt = 0, len(row) - 1
        while lft <= rgt:
            mid = (lft + rgt) // 2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                rgt = mid - 1
            elif row[mid] < target:
                lft = mid + 1

        return False
