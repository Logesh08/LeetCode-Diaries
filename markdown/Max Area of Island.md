# [695. Max Area of Island](https://leetcode.com/problems/max-area-of-island/description/)

You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>'s (representing land) connected **4-directionally**  (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The **area**  of an island is the number of cells with a value <code>1</code> in the island.

Return the maximum **area**  of an island in <code>grid</code>. If there is no island, return <code>0</code>.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;">

```
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

**Example 2:** 

```
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
```

**Constraints:** 

- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 <= m, n <= 50</code>
- <code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.

---

## Solution

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        res = 0
        rows, cols = len(grid), len(grid[0])

        visited = set()

        def bfs(i, j):
            visited.add((i, j))
            queue = deque()
            queue.append((i, j))

            curArea = 1
            while queue:
                i, j = queue.popleft()
                dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for x, y in dirs:
                    r = i + x
                    c = j + y
                    if (0 <= r < rows and 0 <= c < cols and
                        (r, c) not in visited and grid[r][c] == 1):
                        curArea += 1
                        visited.add((r, c))
                        queue.append((r, c))

            return curArea


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, bfs(r, c))

        return res
```