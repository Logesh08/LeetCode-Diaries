from typing import List



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        stack = []

        for i in range(n + 1):
            while stack and  (i == n or heights[stack[-1]] > heights[i]):
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, height * width)
            stack.append(i)


        return maxArea





#############

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
    
# Above is not a O(n) so will not pass

