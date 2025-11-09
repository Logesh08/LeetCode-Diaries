from collections import defaultdict
import heapq
from typing import List

# 7min 10 secs
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1

        freqList = []
        for key, val in hashMap.items():
            freqList.append([key, val])

        freqList.sort(key= lambda x: x[1])

        res = []
        i = 0
        while i < k:
            res.append(freqList.pop()[0])
            i += 1

        return res
    


# 2min 30secs
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)

        for num in nums:
            hashMap[num] += 1

        heap = []

        for key, value in hashMap.items():
            heapq.heappush(heap, (-value, key))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res