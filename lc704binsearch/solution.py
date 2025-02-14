from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lft, rgt = 0, len(nums) - 1
        while lft <= rgt:
            mid = (rgt + lft) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                rgt = mid - 1
            elif target > nums[mid]:
                lft = mid + 1
        return -1
