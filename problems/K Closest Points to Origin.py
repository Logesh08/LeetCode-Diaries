import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            heapq.heappush(minHeap, (sqrt(x*x + y*y), x, y))  # Always remember sqrt is not needed, for comparison!!

        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
    

# Without square root
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x, y in points:
            heapq.heappush(minHeap, (x*x + y*y, x, y))

        res = []
        while k > 0:
            distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res