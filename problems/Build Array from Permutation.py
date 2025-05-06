# LeetCode Problem 1920: Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/


# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

 

# Example 1:

# Input: nums = [0,2,1,5,3,4]
# Output: [0,1,2,4,5,3]
# Explanation: The array ans is built as follows: 
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
#     = [0,1,2,4,5,3]
# Example 2:

# Input: nums = [5,0,1,2,3,4]
# Output: [4,5,0,1,2,3]
# Explanation: The array ans is built as follows:
# ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
#     = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
#     = [4,5,0,1,2,3]
 

# Constraints:

# 1 <= nums.length <= 1000
# 0 <= nums[i] < nums.length
# The elements in nums are distinct.
 

# Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?








# My first apprach with O(n) space

# Too easy beats 100% in the first attempt itself

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans
    


# How is it possible to do it in the O(1)?
# It means we should not create any new array

# We can easily append the items in the same array and 
# return n+1 till 2n, but still the sapce would be increased



# I think when we loop if the element lies in the left side,
# It means it's swapped, else we can use the same

# In case if it's swapped, then we need to look up on the
# Swapped indexes untile its greater than or equal to i


# THIS wont work, ahwww


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            swapIndex = nums[i]
            while swapIndex < i:
                swapIndex = nums[swapIndex]
            nums[i],nums[swapIndex] = nums[swapIndex],nums[i]

        return nums
    



# New approach 

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)
        for i in range(n):
            nums[i] //= n
        return nums
