from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        queue = deque()
        normalFruits = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    normalFruits += 1

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        timeTaken = 0

        while normalFruits > 0 and queue:
            tempQueue = deque()
            for r, c in queue:
                for x, y in dirs:
                    i, j = r + x, c + y
                    if 0 <= i < R and 0 <= j < C and grid[i][j] == 1:
                        grid[i][j] = 2
                        tempQueue.append((i, j))
                        normalFruits -= 1
            timeTaken += 1
            queue = tempQueue              

        return timeTaken if normalFruits == 0 else -1
