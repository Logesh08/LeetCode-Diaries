from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prevIndex = -k -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if i - prevIndex -1 < k:
                    return False
                prevIndex = i
        
        return True