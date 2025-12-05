from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        partitions = 0
    
        right = sum(nums)
        left = 0
        for i in range(n - 1):
            left += nums[i]
            right -= nums[i]
            if (left - right) % 2 == 0:
                partitions += 1

        return partitions

print(Solution().countPartitions([10,10,3,7,6]))
print(Solution().countPartitions([1,2,2]))
print(Solution().countPartitions([2,4,6,8]))