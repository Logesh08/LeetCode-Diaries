from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for val in nums:
            if val-1 not in nums:
                cur = 1
                while val+cur in nums:
                    cur += 1
                longest = max(longest, cur)

        return longest

print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))