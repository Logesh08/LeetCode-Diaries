from typing import List

# 6min 48 secs
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []

        for ind in range(n):
            if ind and nums[ind] == nums[ind - 1]:
                continue

            left = ind + 1
            right = n - 1

            while left < right:
                curSum = nums[ind] + nums[left] + nums[right]
                if curSum == 0:
                    res.append([nums[ind], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                elif curSum > 0:
                    right -= 1
                else:
                    left += 1

        return res