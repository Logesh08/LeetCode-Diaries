from typing import List
from math import sqrt

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDaigonal = -1
        maxArea = -1

        for l,b in dimensions:
            # diag = sqrt(l**2 + b**2) // No need to use this because
            diag = l**2 + b**2         # We are gonna return the area only
            if diag == maxDaigonal:
                maxArea = max(maxArea, l * b)
            elif diag > maxDaigonal:
                maxDaigonal = diag
                maxArea = l * b

        return maxArea
