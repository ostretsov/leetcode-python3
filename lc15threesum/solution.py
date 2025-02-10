from enum import unique
from os import MFD_ALLOW_SEALING
from typing import List


class Solution:
    def sol2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            j = i + 1
            while j < len(nums):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    result.append([nums[i], nums[j], complement])
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        result = []
        seen = {}
        for i0 in range(0, len(nums) - 2):
            if nums[i0] > 0:
                break

            if i0 > 0 and nums[i0 - 1] == nums[i0]:
                continue

            sums = self.twoSum(nums, i0)
            if len(sums) == 0:
                continue
            for twoSum in sums:
                k = f"{nums[i0]}, {twoSum[0]}, {twoSum[1]}"
                if k in seen:
                    continue
                seen[k] = True
                result.append([nums[i0], twoSum[0], twoSum[1]])

        return result

    def twoSum(self, nums: List[int], targetIndex: int) -> List[List[int]]:
        i0, iN = (targetIndex + 1, len(nums) - 1)
        result = []

        while i0 < iN:
            sum = nums[targetIndex] + nums[i0] + nums[iN]
            if sum == 0:
                result.append([nums[i0], nums[iN]])
                i0, iN = (i0 + 1, iN - 1)
            elif sum > 0:
                iN = iN - 1
            elif sum < 0:
                i0 = i0 + 1

        return result

# -1,0,1,2,-1,-4
# -4,-1,-1,0,1,2
