# [3195. Find the Minimum Area to Cover All Ones I](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22)

You are given a 2D **binary**  array <code>grid</code>. Find a rectangle with horizontal and vertical sides with the** smallest**  area, such that all the 1's in <code>grid</code> lie inside this rectangle.

Return the **minimum**  possible area of the rectangle.

**Example 1:** 

<div class="example-block">
Input: grid = [[0,1,0],[1,0,1]]

Output: 6

Explanation:

<img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 279px; height: 198px;">

The smallest rectangle has a height of 2 and a width of 3, so it has an area of <code>2 * 3 = 6</code>.

**Example 2:** 

<div class="example-block">
Input: grid = [[1,0],[0,0]]

Output: 1

Explanation:

<img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 204px; height: 201px;">

The smallest rectangle has both height and width 1, so its area is <code>1 * 1 = 1</code>.

**Constraints:** 

- <code>1 <= grid.length, grid[i].length <= 1000</code>
- <code>grid[i][j]</code> is either 0 or 1.
- The input is generated such that there is at least one 1 in <code>grid</code>.

---

## Solution

```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        maxBreadth = maxHeight =  minBreadth = minHeight = -1

        for i in range(R):
            if 1 in grid[i]:
                minHeight = i
                break

        for i in range(R)[::-1]:
            if 1 in grid[i]:
                maxHeight = i
                break

        for j in range(C):
            for i in range(R):
                if grid[i][j] == 1:
                    minBreadth = j
                    break
            if minBreadth > -1: break

        for j in range(C)[::-1]:
            for i in range(R):
                if grid[i][j] == 1:
                    maxBreadth = j
                    break
            if maxBreadth > -1: break

        return (maxBreadth - minBreadth + 1) * (maxHeight - minHeight + 1)
```