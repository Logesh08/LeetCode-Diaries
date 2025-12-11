from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        res = 0
        maxRows = [0] * (n + 1)
        maxCols = [0] * (n + 1)
        minRows = [float("inf")] * (n + 1)
        minCols = [float("inf")] * (n + 1)

        for x, y in buildings:
            maxRows[x] = max(maxRows[x], y)
            minRows[x] = min(minRows[x], y)

            maxCols[y] = max(maxCols[y], x)
            minCols[y] = min(minCols[y], x)

        for x, y in buildings:
            if (minRows[x] < y < maxRows[x] and
                minCols[y] < x < maxCols[y]):
                res += 1

        return res