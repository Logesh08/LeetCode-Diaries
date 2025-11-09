from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                gridInd = ((i//3)*3) + j//3
                if num in row[i] or num in col[j] or num in grid[gridInd]:
                    return False
                row[i].add(num)
                col[j].add(num)
                grid[gridInd].add(num)

        return True