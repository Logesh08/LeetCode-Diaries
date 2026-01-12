# [1266. Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/description/?envType=daily-question&envId=2026-01-12)

On a 2D plane, there are <code>n</code> points with integer coordinates <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. Return the **minimum time**  in seconds to visit all the points in the order given by <code>points</code>.

You can move according to these rules:

- In <code>1</code> second, you can either:

- move vertically by oneunit,
- move horizontally by one unit, or
- move diagonally <code>sqrt(2)</code> units (in other words, move one unit vertically then one unit horizontally in <code>1</code> second).

- You have to visit the points in the same order as they appear in the array.
- You are allowed to pass through points that appear later in the order, but these do not count as visits.

**Example 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/14/1626_example_1.PNG" style="width: 500px; height: 428px;">

```
Input: points = [[1,1],[3,4],[-1,0]]
Output: 7
Explanation: One optimal path is **[1,1]**  -> [2,2] -> [3,3] -> **[3,4] ** -> [2,3] -> [1,2] -> [0,1] -> **[-1,0]**    
Time from [1,1] to [3,4] = 3 seconds 
Time from [3,4] to [-1,0] = 4 seconds
Total time = 7 seconds
```

**Example 2:** 

```
Input: points = [[3,2],[-2,2]]
Output: 5
```

**Constraints:** 

- <code>points.length == n</code>
- <code>1 <= n<= 100</code>
- <code>points[i].length == 2</code>
- <code>-1000<= points[i][0], points[i][1]<= 1000</code>

---

## Solution

```python
class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        res = 0

        for i in range(1, len(p)):
            x1, y1 = p[i - 1]
            x2, y2 = p[i]
            res += max(abs(x2 - x1), abs(y2 - y1))

        return res
```