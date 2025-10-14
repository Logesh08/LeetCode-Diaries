from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        left = []
        right = []
        for i in range(len(nums)):
            if not left:
                left.append(nums[i])
            elif len(left) < k and left[-1] < nums[i]:
                left.append(nums[i])
            elif not right:
                right.append(nums[i])
            elif len(right) < k and right[-1] < nums[i]:
                right.append(nums[i])
            elif len(right) == len(left):
                return True
            else:
                left = [nums[i]]
                right = []

        return False


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            if nums[i] >nums[i - 1]:
                dp[i] += dp[i - 1]

        for window in range(n - 2 * k + 1):
            if dp[window + k - 1] >= k and dp[window + 2*k - 1] >= k:
                return True
        
        return False
