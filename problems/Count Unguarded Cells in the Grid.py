from typing import List

# Not optimal solution, optimal solution is available below
class Solution:
    def countUnguarded(self, n: int, m: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        EMPTY, GUARD, WALL, RAY = 0, 1, 2, 3
        matrix = [[0]*m for _ in range(n)]
        ungaurded = (m * n) - len(guards) - len(walls)
        for r,c in walls:
            matrix[r][c] = WALL
        for r,c in guards:
            matrix[r][c] = GUARD

        dirs = ((0,1),(1,0),(-1,0),(0,-1))
        for guard in guards:
            for dir in dirs:
                dx = guard[0] + dir[0]
                dy = guard[1] + dir[1]
                while 0 <= dx < n and 0 <= dy < m and matrix[dx][dy] != WALL and matrix[dx][dy] != GUARD:
                    if matrix[dx][dy] == EMPTY:
                        matrix[dx][dy] = RAY
                        ungaurded -= 1
                    dx += dir[0]
                    dy += dir[1]

        return ungaurded
        


### Top solution from leetcode:
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for _ in range(m)]
        for r,c in walls:
            grid[r][c] = 1
        for r,c in guards:
            grid[r][c] = 1
        for r,c in guards:
            u = r-1
            while u >= 0 and grid[u][c] != 1:
                grid[u][c] = 2
                u -= 1
            d = r+1
            while d < m and grid[d][c] != 1:
                grid[d][c] = 2
                d += 1
            l = c-1
            while l >= 0 and grid[r][l] != 1:
                grid[r][l] = 2
                l -= 1
            ri = c+1
            while ri < n and grid[r][ri] != 1:
                grid[r][ri] = 2
                ri += 1
        unguarded = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    unguarded += 1
        return unguarded