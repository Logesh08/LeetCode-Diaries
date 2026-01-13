# [3453. Separate Squares I](https://leetcode.com/problems/separate-squares-i/description/?envType=daily-question&envId=2026-01-13)

You are given a 2D integer array <code>squares</code>. Each <code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code> represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the **minimum**  y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within <code>10^-5</code> of the actual answer will be accepted.

**Note** : Squares **may**  overlap. Overlapping areas should be counted **multiple times** .

**Example 1:** 

<div class="example-block">
Input: squares = [[0,0,1],[2,2,1]]

Output: 1.00000

Explanation:

<img alt="" src="https://assets.leetcode.com/uploads/2025/01/06/4062example1drawio.png" style="width: 378px; height: 352px;">

Any horizontal line between <code>y = 1</code> and <code>y = 2</code> will have 1 square unit above it and 1 square unit below it. The lowest option is 1.

**Example 2:** 

<div class="example-block">
Input: squares = [[0,0,2],[1,1,1]]

Output: 1.16667

Explanation:

<img alt="" src="https://assets.leetcode.com/uploads/2025/01/15/4062example2drawio.png" style="width: 378px; height: 352px;">

The areas are:

- Below the line: <code>7/6 * 2 (Red) + 1/6 (Blue) = 15/6 = 2.5</code>.
- Above the line: <code>5/6 * 2 (Red) + 5/6 (Blue) = 15/6 = 2.5</code>.

Since the areas above and below the line are equal, the output is <code>7/6 = 1.16667</code>.

**Constraints:** 

- <code>1 <= squares.length <= 5 * 10^4</code>
- <code>squares[i] = [x<sub>i</sub>, y<sub>i</sub>, l<sub>i</sub>]</code>
- <code>squares[i].length == 3</code>
- <code>0 <= x<sub>i</sub>, y<sub>i</sub> <= 10^9</code>
- <code>1 <= l<sub>i</sub> <= 10^9</code>
- The total area of all the squares will not exceed <code>10^12</code>.

---

## Solution

```python
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        totalArea = 0.0
        minY = float("inf")
        maxY = float("-inf")

        for x, y, l in squares:
            totalArea += l * l
            minY = min(minY, y)
            maxY = max(maxY, y + l)

        target = totalArea / 2.0

        def findAreaAbove(h: float) -> float:
            area = 0.0
            for x, y, l in squares: 
                if y > h:
                    # these are fully available sqares
                    area += l * l
                elif y + l > h:
                    # these squares are being cut through
                    area += (y + l  - h) * l
                else:
                    # skip squares at bottom
                    pass
            return area
        
        low, high = minY, maxY
        tolerance = 1e-5

        while high - low > tolerance:
            mid = (low + high) / 2.0
            areaAbove = findAreaAbove(mid)
            if areaAbove > target:
                low = mid
            else:
                high = mid

        return (low + high) / 2.0
```