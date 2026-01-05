from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        maxSum = 0
        minAbs = float("inf")
        noOfNeg = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = matrix[i][j]
                maxSum += abs(val)
                minAbs = min(minAbs, abs(val))
                if val < 0:
                    noOfNeg += 1

        return maxSum if noOfNeg % 2 == 0 else maxSum - (2 * minAbs)
