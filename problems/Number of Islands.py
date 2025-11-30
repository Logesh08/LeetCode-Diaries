from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        res = 0
        rows, cols = len(grid), len(grid[0])

        visited = set()
        def bfs(i, j):
            visited.add((i, j))
            queue = deque()
            queue.append((i, j))

            while queue:
                i,j = queue.popleft()
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in dirs:
                    r = i + dx
                    c = j + dy
                    if (0 <= r < rows and 0 <= c < cols and
                        grid[r][c] == "1" and (r,c) not in visited):
                        visited.add((r, c))
                        queue.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    bfs(r, c)

        return res