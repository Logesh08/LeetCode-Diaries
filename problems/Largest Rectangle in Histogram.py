from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        for ind in range(n):
            left = right = ind
            while 0 <= left-1 < n and heights[left-1] >= heights[ind]:
                left -= 1
            while 0 <= right+1 < n and heights[right+1] >= heights[ind]:
                right += 1
            width = right - left + 1
            ans = max(ans, heights[ind] * width)

        return ans