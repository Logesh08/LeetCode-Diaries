from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        stack = []
        for i in range(n + 1):
            while stack and (i == n or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                if not stack:
                    width = i
                    # means its the only element, that is the smallest element so far, so it can expand
                    # fully to the left, that why we use "i", means 0 -> i 
                else:
                    width = i - stack[-1] - 1 
                    # Notice that we are using stack[-1], that means the previous smallest height
                    # which we can extend to.
                    # First i got confused and used it without poping, meaning the current top,
                    # but the original goal here is to actually extend to the left as well, doing so
                    # we actually satisfy that!

                    # eg indexes stack = [3, 5] and we encounter something smaller called i=x,
                    # now we need to calculate the width for i=5 , using 3 as starting and i-1 as ending
                    # so that for i=x it becomes, height[5] * (i-3-1)

                ans = max(ans, height * width)      
            stack.append(i)
        return ans