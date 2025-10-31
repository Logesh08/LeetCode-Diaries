# The Two Sneaky Numbers of Digitville

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashSet = set()
        ans = []
        for num in nums:
            if num in hashSet:
                ans.append(num)
            else:
                hashSet.add(num)
        return ans