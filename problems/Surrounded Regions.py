from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        rows, cols = len(board), len(board[0])

        def dfs(i, j):
            if (0 <= i < rows and 0 <= j < cols and
                board[i][j] == 'O' and (i, j) not in visited):
                visited.add((i, j))
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i - 1, j)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in visited:
                    board[i][j] = 'X'