# [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/description/?envType=daily-question&envId=2026-01-11)

Given a <code>rows x cols</code>binary <code>matrix</code> filled with <code>0</code>'s and <code>1</code>'s, find the largest rectangle containing only <code>1</code>'s and return its area.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;">

```
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
```

**Example 2:** 

```
Input: matrix = [["0"]]
Output: 0
```

**Example 3:** 

```
Input: matrix = [["1"]]
Output: 1
```

**Constraints:** 

- <code>rows == matrix.length</code>
- <code>cols == matrix[i].length</code>
- <code>1 <= rows, cols <= 200</code>
- <code>matrix[i][j]</code> is <code>'0'</code> or <code>'1'</code>.

---

## Solution

```python
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_area = 0
        heights = [0] * (len(matrix[0]) + 1)

        for row in matrix:
            for i in range(len(row)):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0

            stack = []
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area
```