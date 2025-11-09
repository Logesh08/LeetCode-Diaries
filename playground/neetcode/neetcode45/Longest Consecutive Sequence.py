from typing import List

# 2min 13 secs
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for num in nums:
            if num-1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                if length > longest:
                    longest = length

        return longest