from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        res = []

        left = 0
        for right in range(len(nums)):
            while window and nums[window[-1]] <= nums[right]:
                window.pop()
            window.append(right)

            if left > window[0]:
                window.popleft()

            if (right + 1) >= k:
                res.append(nums[window[0]])
                left += 1

        return res

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))