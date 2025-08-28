from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for k in range(n):
            r, c = k, 0
            vals = []
            while r < n and c < n:
                vals.append(grid[r][c])
                r += 1; c += 1
            vals.sort(reverse=True)
            r, c = k, 0
            i = 0
            while r < n and c < n:
                grid[r][c] = vals[i]
                i += 1; r += 1; c += 1


        for k in range(1, n):
            r, c = 0, k
            vals = []
            while r < n and c < n:
                vals.append(grid[r][c])
                r += 1; c += 1
            vals.sort()
            r, c = 0, k
            i = 0
            while r < n and c < n:
                grid[r][c] = vals[i]
                i += 1; r += 1; c += 1

        return grid
