from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if all(nums):
            return(len(nums)-1)
        
        if sum(nums) == 0:
            return(0)

        leftSeen = False
        prevZero = left = -1
        singleZero = 0      # Only allowed case

        ans = 0

        for right in range(len(nums)):
            if nums[right] == 1:
                if not leftSeen:
                    leftSeen = True
                    left = right
                ans = max(ans, right - left + 1 - singleZero)
            else:
                if not singleZero and leftSeen:
                    singleZero = 1
                elif leftSeen:
                    left = max(left, prevZero + 1)
                    singleZero = 1
                prevZero = right

        return ans
