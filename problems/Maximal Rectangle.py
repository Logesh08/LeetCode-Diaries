from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        r = len(matrix)
        c = len(matrix[0])
        res = 0
        heights = [0] * c

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            res = max(res, self.largestRectangleArea(heights))

        return res
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                curHeight = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                largest = max(largest, curHeight * width)
            stack.append(i)

        return largest