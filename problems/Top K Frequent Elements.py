from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1

        freqList = []
        for key, value in freqMap.items():
            freqList.append([key, value])

        freqList.sort(key= lambda x: x[1])

        i = 0
        ans = []
        while i < k:
            item = freqList.pop()
            ans.append(item[0])
            i += 1

        return ans