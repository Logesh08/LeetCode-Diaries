from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            maxArea = max(maxArea, h * w)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maxArea