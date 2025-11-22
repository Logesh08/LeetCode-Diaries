from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minOperations = 0
        
        for num in nums:
            remaing = num % 3
            if remaing:
                minOperations += 1

        return minOperations