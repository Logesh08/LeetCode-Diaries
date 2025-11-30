from collections import deque
from typing import List


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