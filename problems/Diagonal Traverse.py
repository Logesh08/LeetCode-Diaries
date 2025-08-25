from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        for d in range(m + n - 1):
            i_lo = max(0, d - (n - 1))
            i_hi = min(m - 1, d)
            if d % 2 == 0:
                for i in range(i_hi, i_lo - 1, -1):
                    res.append(mat[i][d - i])
            else:
                for i in range(i_lo, i_hi + 1):
                    res.append(mat[i][d - i])
        return res
    

# Much better and best solution, The fastest!

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        i = j = 0
        direction = 1
        for _ in range(m*n):
            res.append(mat[i][j])
            if direction == 1:
                if j == n-1:
                    i += 1
                    direction = -1
                elif i == 0:
                    j += 1
                    direction = -1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1
                    direction = 1
                elif j == 0:
                    i += 1
                    direction = 1
                else:
                    i += 1
                    j -= 1
        return res