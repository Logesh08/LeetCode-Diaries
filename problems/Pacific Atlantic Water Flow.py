from typing import List


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