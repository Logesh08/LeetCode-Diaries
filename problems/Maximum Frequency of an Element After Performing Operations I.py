# Maximum Frequency of an Element After Performing Operations I

from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        maxNum = max(nums)
        minNum = min(nums)

        freq = [0] * (maxNum + 1)
        pref = [0] * (maxNum + 1)

        for num in nums:
            freq[num] += 1
        for i in range(1, maxNum+1):
            pref[i] = pref[i - 1] + freq[i]

        ans = 1

        for i in range(minNum, maxNum+1):
            left = max(i - k - 1, 0)
            right = min(i + k, maxNum)
            total = min(pref[right] - pref[left], freq[i] + numOperations)
            if total > ans:
                ans = total

        return ans



























class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        max_num = nums[-1]
        min_num = nums[0]


        freq = [0] * (max_num + 1)
        cums = [0] * (max_num + 1)

        for num in nums:
            freq[num] += 1
        for i in range(1, max_num + 1):
            cums[i] = cums[i - 1] + freq[i]

        res = 0
        for i in range(min_num, max_num + 1):
            l = max(0, i - k - 1)
            r = min(max_num, i + k)
            tot = min(cums[r] - cums[l], freq[i] + numOperations)
            if tot > res:
                res = tot

        return res