from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        prev = 0
        ans = 0
        for num in nums:
            if num == 0:
                ans += prev + 1
                prev += 1
            else:
                prev = 0
        return ans