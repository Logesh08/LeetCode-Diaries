from typing import List

# 2min 3secs
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            carry = target - num
            if carry in hashMap:
                return [hashMap[carry], i]
            hashMap[num] = i