from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MODULO = 10**9 + 7
        hashMap = defaultdict(int) # gonna map no of points 
                                   # available in an horizontal line
        for x, y in points:
            hashMap[y] += 1

        # now every y having value grater than 1 is eleigible to form 
        # trapezoids, but how to count the number ?
        
        # for y1 = 2 and y2 = 2, we can actually make 1 trapezoid
        # for y1 = 2 and y2 = 3, we can make 3 trapezoids...
        # So we can formulate that...
        # 2 pts -> 1 segment
        # 3 pts -> 3 segments
        # segments = pts * (pts - 1) // 2
        # 2 pts -> segments = 2 * (2 - 1) // 2 => 1
        # 3 pts -> segments = 3 * (3 - 1) // 2 => 3

        result = 0
        totalSegs = 0
        for pts in hashMap.values():
            if pts > 1:
                segments = pts * (pts - 1) // 2
                result = segments * totalSegs
                totalSegs += segments

        return result % MODULO