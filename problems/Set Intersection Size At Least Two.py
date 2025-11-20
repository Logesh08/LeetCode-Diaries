from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key = lambda i: (i[1],-i[0]))
        p1 = -1
        p2 = -1

        for left, right in intervals:
            if left > p2:
                res += 2
                p1, p2 = right - 1, right
            elif p1 < left:
                res += 1
                p1, p2 = p2, right
            else:
                # Both lies in same point
                pass

        return res