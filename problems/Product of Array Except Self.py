from typing import List

# My pavapatta solution!
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] * nums[i])
        for i in range(len(nums)-2,-1,-1):
            suffix.append(suffix[-1] * nums[i])
        suffix.reverse()

        ans = [suffix[1]]

        for i in range(1,len(nums)-1):
            ans.append(prefix[i-1] * suffix[i+1])

        ans.append(prefix[-2])
        return ans
    

# Optimal
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

Solution().productExceptSelf([1,2,3,4])