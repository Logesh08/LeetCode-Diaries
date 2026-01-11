from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        sum = 0

        for num in nums:
            sum += num
            res = max(res, sum)
            if sum < 0:
                sum = 0

        return res