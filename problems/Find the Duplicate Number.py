from typing import List


# Yay I learnt floyd's Algorithm today

# This is not standard case but this problem can be solved by Floyd's Algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                # Fast and slow intersection point

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
                # Old and new slow intersection point
                # This is the place where the cycle begins
                # Cyble begins means, 2 or more nodes point to a same node
                # In this case for ex nums[i] = 2, nums[j] = 2, since both point here
                # This is where the cycle begins and the answer is also the same!

        return nums[slow]



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