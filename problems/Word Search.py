from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]

        res = [False]

        def dfs(i, j, chInd):
            if res[0]:
                return
            if word[chInd] != board[i][j]:
                return
            if chInd == len(word) - 1:
                res[0] = True
                return
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dx = i + x
                dy = j + y
                if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy]:
                    visited[i][j] = True
                    dfs(dx, dy, chInd + 1)
                    visited[i][j] = False
                    

        for i in range(n):
            for j in range(m):
                dfs(i, j, 0)
                if res[0]:
                    return True

        return res[0]
    



