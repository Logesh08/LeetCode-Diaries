from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        left = 0
        right = r*c - 1

        while left <= right:
            mid = left + (right - left) // 2
            i = mid // c
            j = mid % c
            cur = matrix[i][j]
            if cur > target:
                right = mid - 1
            elif cur < target:
                left = mid + 1
            else:
                return True
        
        return False