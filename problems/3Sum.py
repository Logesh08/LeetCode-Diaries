from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur > 0:
                    right -= 1
                elif cur < 0:
                    left += 1
                else:
                    ans.append([nums[i] , nums[left] , nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return ans
    



# A lil optimized version
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur > 0:
                    right -= 1
                elif cur < 0:
                    left += 1
                else:
                    ans.append([nums[i] , nums[left] , nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and right > left:
                        right -= 1

        return ans