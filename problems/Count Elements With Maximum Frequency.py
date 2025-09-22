from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        heiestFreq = -1
        ans = 0

        for num in nums:
            freq[num] += 1
            heiestFreq = max(heiestFreq, freq[num])

        for val in freq.values():
            if val == heiestFreq:
                ans += val

        return ans