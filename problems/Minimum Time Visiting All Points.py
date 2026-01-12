from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        res = 0

        for i in range(1, len(p)):
            x1, y1 = p[i - 1]
            x2, y2 = p[i]
            res += max(abs(x2 - x1), abs(y2 - y1))

        return res