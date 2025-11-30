# [417. Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)

There is an <code>m x n</code> rectangular island that borders both the **Pacific Ocean**  and **Atlantic Ocean** . The **Pacific Ocean**  touches the island's left and top edges, and the **Atlantic Ocean**  touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an <code>m x n</code> integer matrix <code>heights</code> where <code>heights[r][c]</code> represents the **height above sea level**  of the cell at coordinate <code>(r, c)</code>.

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is **less than or equal to**  the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a **2D list**  of grid coordinates <code>result</code> where <code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> denotes that rain water can flow from cell <code>(r<sub>i</sub>, c<sub>i</sub>)</code> to **both**  the Pacific and Atlantic oceans.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" style="width: 400px; height: 400px;">

```
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
      [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
      [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
      [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
      [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
      [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
      [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
```

**Example 2:** 

```
Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
```

**Constraints:** 

- <code>m == heights.length</code>
- <code>n == heights[r].length</code>
- <code>1 <= m, n <= 200</code>
- <code>0 <= heights[r][c] <= 10^5</code>

---

## Solution

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        res = []

        def dfs(i, j, visited, previous):
            if (0 <= i < rows and 0 <= j < cols and
                (i, j) not in visited and heights[i][j] >= previous):
                visited.add((i, j))
                dfs(i + 1, j, visited, heights[i][j])
                dfs(i, j + 1 ,visited, heights[i][j])
                dfs(i - 1, j, visited, heights[i][j])
                dfs(i, j - 1, visited, heights[i][j])

        for r in range(rows):
            dfs(r, 0, pacific, -1)
            dfs(r, cols - 1, atlantic, -1)

        for c in range(cols):
            dfs(0, c, pacific, -1)
            dfs(rows - 1, c, atlantic, -1)


        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i, j])

        return res
```