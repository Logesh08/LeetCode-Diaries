from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rotateBoard = [list(r) for r in zip(*board[::-1])]

        for i in range(9):
            row = {}
            col = {}
            for j in range(9):
                if board[i][j] != '.':
                    row[board[i][j]] = row.get(board[i][j], 0) + 1
                    if row[board[i][j]] == 2:
                        return False
                if rotateBoard[i][j] != '.':
                    col[rotateBoard[i][j]] = col.get(rotateBoard[i][j], 0) + 1
                    if col[rotateBoard[i][j]] == 2:
                        return False
                    

            box = {}
            cent = [i//3 , i%3]
            for n in range(3):
                for m in range(3):
                    val = board[n + cent[0]*3][m + cent[1]*3]
                    if val != '.':
                        box[val] = box.get(val, 0) + 1
                        if box[val] == 2:
                            return False
            

        return True