from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ans = 0

        for i in range(col):
            ans += matrix[0][i]

        for i in range(1, row):
            ans += matrix[i][0]

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    # top = matrix[i-1][j]
                    # left = matrix[i][j-1]
                    # daig = matrix[i-1][j-1]
                    # matrix[i][j] += min(top, left, daig)
                    matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                    ans += matrix[i][j]

        return ans