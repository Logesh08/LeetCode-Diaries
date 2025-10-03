# [407. Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/description/?envType=daily-question&envId=2025-10-03)

Given an <code>m x n</code> integer matrix <code>heightMap</code> representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg" style="width: 361px; height: 321px;">

```
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg" style="width: 401px; height: 321px;">

```
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
```

**Constraints:** 

- <code>m == heightMap.length</code>
- <code>n == heightMap[i].length</code>
- <code>1 <= m, n <= 200</code>
- <code>0 <= heightMap[i][j] <= 2 * 10^4</code>

---

## Solution

```python
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])
        if n < 3 or m < 3:
            return 0


        visited = [[False] * m for _ in range(n)]
        heap = []

        def push(i, j, level):
            if not visited[i][j]:
                visited[i][j] = True
                heapq.heappush(heap, (level, i, j))

        # seed all borders
        for i in range(n):
            push(i, 0, heightMap[i][0])
            push(i, m - 1, heightMap[i][m - 1])
        for j in range(m):
            push(0, j, heightMap[0][j])
            push(n - 1, j, heightMap[n - 1][j])

        ans = 0
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            level, r, c = heapq.heappop(heap)
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    nh = heightMap[nr][nc]
                    if nh < level:
                        ans += level - nh
                        push(nr, nc, level)  # water fills up to current rim
                    else:
                        push(nr, nc, nh)     # higher ground becomes new rim

        return ans
```