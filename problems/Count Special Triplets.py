from collections import defaultdict
from typing import List


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        right = defaultdict(int)
        left = defaultdict(int)
        res = 0

        for num in nums:
            right[num] += 1
        
        for num in nums:
            right[num] -= 1

            cur = num * 2
            if right[cur] and left[cur]:
                res += right[cur] * left[cur]

            left[num] += 1

        return res % MOD