from collections import deque
from typing import List

# 7mins
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
        