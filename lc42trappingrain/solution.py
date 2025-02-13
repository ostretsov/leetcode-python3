from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        while i < len(height) and height[i] == 0:
            i += 1

        j = len(height) - 1
        while 0 < j < len(height) and height[j] == 0:
            j -= 1

        height = height[i:j+1]

        water = 0

        stack = []
        i = 0
        while i < len(height):
            lake_left_border, lake_right_border = i, i
            while stack and height[stack[-1]] <= height[i]:
                lake_left_border = stack.pop()

            if lake_right_border - lake_left_border > 1:
                water += self.lake_size(height, lake_left_border, lake_right_border)

            stack.append(i)
            i += 1

        stack = []
        i = 0
        height.reverse()
        while i < len(height):
            lake_left_border, lake_right_border = i, i
            while stack and height[stack[-1]] <= height[i]:
                lake_left_border = stack.pop()

            if lake_right_border - lake_left_border > 1:
                water += self.lake_size(height, lake_left_border, lake_right_border)

            stack.append(i)
            i += 1

        return water

    def lake_size(self, height: List[int], i: int, j: int) -> int:
        water = 0

        maxWaterLevel = min(height[i], height[j])
        idx = i + 1
        while idx < j:
            waterDiff = (maxWaterLevel - height[idx])
            height[idx] += waterDiff
            water += waterDiff
            idx += 1

        return water

