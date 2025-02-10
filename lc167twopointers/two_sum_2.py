from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers)-1
        while i1 < i2:
            sum = numbers[i1] + numbers[i2]
            if sum == target:
                break
            elif sum < target:
                i1 = i1 + 1
            elif sum > target:
                i2 = i2 - 1

        return [i1 + 1, i2 + 1]

    def twoSumOnePassHashTable(self, numbers: List[int], target: int) -> List[int]:
        ht = {}
        for i in range(len(numbers)):
            compliment = target - numbers[i]
            if compliment in ht:
                return [ht[compliment]+1, i+1]
            ht[numbers[i]] = i


