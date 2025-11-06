from typing import List





# Both sols will fail actually below, ones
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != nums[i] - 1 and nums[nums[i] - 1] == nums[i]:
                return nums[i]
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i != nums[i] and nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]