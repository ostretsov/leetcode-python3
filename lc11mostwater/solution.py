from typing import List

# https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        maxH = 0
        maxHj = len(height) - 1
        i = 0
        while i < len(height) - 1:
            if height[i] == 0:
                i += 1
                continue

            if maxH >= height[i]:
                i += 1
                continue

            j = maxHj
            if (j - i) * height[i] <= maxA:
                i += 1
                continue

            while j > i:
                if height[j] == 0:
                    j -= 1
                    continue

                if height[j] < height[maxHj]:
                    j -= 1
                    continue

                sqL = j - i
                sqH = min(height[i], height[j])
                sqA = sqL * sqH
                if sqA > maxA:
                    maxH = sqH
                    maxHj = j
                    maxA = sqA

                j -= 1

            i += 1

        return maxA

    def maxArea2(self, height: List[int]) -> int:
        maxA = 0
        i = 0
        j = len(height) - 1
        while i < j:
            a = (j - i) * min(height[i], height[j])
            if a > maxA:
                maxA = a
            if height[i] == height[j]:
                i += 1
                j -= 1
            elif height[i] < height[j]:
                i += 1
            elif height[j] < height[i]:
                j -= 1
        return maxA