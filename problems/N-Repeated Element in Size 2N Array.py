from collections import defaultdict
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1
            if hashMap[num] == n:
                return num