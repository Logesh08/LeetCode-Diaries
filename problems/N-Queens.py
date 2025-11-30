from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        cols = set()
        negDiag = set()
        posDiag = set()
        board = [['.'] * n for _ in range(n)]
        def dfs(i: int) -> None:
            if i == n:
                res.append(["".join(row) for row in board])
                return

            for j in range(n):
                if j not in cols and i + j not in posDiag and i - j not in negDiag:
                    cols.add(j)
                    posDiag.add(i + j)
                    negDiag.add(i - j)
                    board[i][j] = 'Q'
                    dfs(i + 1)
                    board[i][j] = '.'
                    cols.remove(j)
                    posDiag.remove(i + j)
                    negDiag.remove(i - j)

        dfs(0)
        return res
