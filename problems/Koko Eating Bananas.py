from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            k = mid
            hour = 0
            for pile in piles:
                hour += ceil(pile / k)
            if hour > h:
                left = mid + 1
            else:
                right = mid
                # notice that its mid and not mid - 1, because inclusive.

        return left







### Bruteforce - TLE
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = -1

        for k in range(1, right+1)[::-1]:
            hour = 0
            for pile in piles:
                hour += ceil(pile / k)
            if hour > h:
                break
            ans = k
        return ans

        # while left <= right:
        #     k = 