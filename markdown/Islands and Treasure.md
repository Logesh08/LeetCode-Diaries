# Islands and Treasure

**Difficulty:** Medium

## Problem Description

You are given a `m × n` 2D grid initialized with these three possible values:

- `-1` - A water cell that can not be traversed.
- `0` - A treasure chest.
- `INF` - A land cell that can be traversed. We use the integer `2^31 - 1 = 2147483647` to represent `INF`.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain `INF`.

Assume the grid can only be traversed **up, down, left, or right**.

**Note:** Modify the grid in-place.

---

## Examples

**Example 1:**

**Input:**
```
[
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
```

**Output:**
```
[
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]
```

**Example 2:**

**Input:**
```
[
  [0,-1],
  [2147483647,2147483647]
]
```

**Output:**
```
[
  [0,-1],
  [1,2]
]
```

---

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 100`
- `grid[i][j]` is one of `{-1, 0, 2147483647}`


---

## Solutions

```python
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        R = len(grid)
        C = len(grid[0])
        INF = 2147483647
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            tempQueue = deque()
            for i, j in queue:
                for x, y in dirs:
                    r = i + x
                    c = j + y
                    if 0 <= r < R and 0 <= c < C and grid[r][c] == INF:
                        grid[r][c] = grid[i][j] + 1
                        tempQueue.append((r, c))
            queue = tempQueue
```