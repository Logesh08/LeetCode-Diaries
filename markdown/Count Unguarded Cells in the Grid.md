# [2257. Count Unguarded Cells in the Grid](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/description/?envType=daily-question&envId=2025-10-31)

You are given two integers <code>m</code> and <code>n</code> representing a **0-indexed**  <code>m x n</code> grid. You are also given two 2D integer arrays <code>guards</code> and <code>walls</code> where <code>guards[i] = [row<sub>i</sub>, col<sub>i</sub>]</code> and <code>walls[j] = [row<sub>j</sub>, col<sub>j</sub>]</code> represent the positions of the <code>i^th</code> guard and <code>j^th</code> wall respectively.

A guard can see <b>every</b> cell in the four cardinal directions (north, east, south, or west) starting from their position unless **obstructed**  by a wall or another guard. A cell is **guarded**  if there is **at least**  one guard that can see it.

Return the number of unoccupied cells that are **not**  **guarded** .

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example1drawio2.png" style="width: 300px; height: 204px;">

```
Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2022/03/10/example2drawio.png" style="width: 200px; height: 201px;">

```
Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
```

**Constraints:** 

- <code>1 <= m, n <= 10^5</code>
- <code>2 <= m * n <= 10^5</code>
- <code>1 <= guards.length, walls.length <= 5 * 10^4</code>
- <code>2 <= guards.length + walls.length <= m * n</code>
- <code>guards[i].length == walls[j].length == 2</code>
- <code>0 <= row<sub>i</sub>, row<sub>j</sub> < m</code>
- <code>0 <= col<sub>i</sub>, col<sub>j</sub> < n</code>
- All the positions in <code>guards</code> and <code>walls</code> are **unique** .

---

## Solution

```python
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # 0 empty, 1 blocker (wall/guard), 2 guarded
        grid = [[0]*n for _ in range(m)]
        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 1

        # alias for speed
        G = grid

        for r, c in guards:
            # up
            rr = r - 1
            while rr >= 0 and G[rr][c] != 1:
                G[rr][c] = 2
                rr -= 1
            # down
            rr = r + 1
            while rr < m and G[rr][c] != 1:
                G[rr][c] = 2
                rr += 1
            # left
            cc = c - 1
            row = G[r]
            while cc >= 0 and row[cc] != 1:
                row[cc] = 2
                cc -= 1
            # right
            cc = c + 1
            row = G[r]
            while cc < n and row[cc] != 1:
                row[cc] = 2
                cc += 1

        # count zeros
        unguarded = 0
        for r in range(m):
            row = G[r]
            for c in range(n):
                if row[c] == 0:
                    unguarded += 1
        return unguarded
```