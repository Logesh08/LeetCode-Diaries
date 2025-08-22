from typing import List

# My initial solution, seems practical but the worst possible solution cuz 
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        maxBreadth = maxHeight = float("-inf")
        minBreadth = minHeight = float("inf")

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxHeight = max(maxHeight, i)
                    minHeight = min(minHeight, i)
                    maxBreadth = max(maxBreadth, j)
                    minBreadth = min(minBreadth, j)

        return (maxBreadth - minBreadth + 1) * (maxHeight - minHeight + 1)
    


# What if we just use 4 loops to find those?
# This is the most optimal and best solution
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        maxBreadth = maxHeight =  minBreadth = minHeight = -1

        for i in range(R):
            if 1 in grid[i]:
                minHeight = i
                break

        for i in range(R)[::-1]:
            if 1 in grid[i]:
                maxHeight = i
                break

        for j in range(C):
            for i in range(R):
                if grid[i][j] == 1:
                    minBreadth = j
                    break
            if minBreadth > -1: break

        for j in range(C)[::-1]:
            for i in range(R):
                if grid[i][j] == 1:
                    maxBreadth = j
                    break
            if maxBreadth > -1: break

        return (maxBreadth - minBreadth + 1) * (maxHeight - minHeight + 1)



# More pythonic version
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        top = next((i for i in range(R) if 1 in grid[i]), -1)
        if top == -1:
            return 0
        bottom = next((i for i in range(R-1, -1, -1) if 1 in grid[i]), -1)

        left = next((j for j in range(C) if any(grid[i][j] == 1 for i in range(R))), -1)
        right = next((j for j in range(C-1, -1, -1) if any(grid[i][j] == 1 for i in range(R))), -1)

        return (right - left + 1) * (bottom - top + 1)
