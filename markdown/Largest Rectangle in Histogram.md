# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/description/)

Given an array of integers <code>heights</code> representing the histogram's bar height where the width of each bar is <code>1</code>, return the area of the largest rectangle in the histogram.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" style="width: 522px; height: 242px;">

```
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" style="width: 202px; height: 362px;">

```
Input: heights = [2,4]
Output: 4
```

**Constraints:** 

- <code>1 <= heights.length <= 10^5</code>
- <code>0 <= heights[i] <= 10^4</code>

---

## Solution

```python
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
```