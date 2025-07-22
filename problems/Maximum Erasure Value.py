# LeetCode Problem 1695: Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/


# You are given an array of positive integers nums and want to erase a subarray containing unique elements.
# The score you get by erasing the subarray is equal to the sum of its elements.

# Return the maximum score you can get by erasing exactly one subarray.

# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is,
# if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 


# Example 1:
# Input: nums = [4,2,4,5,6]
# Output: 17
# Explanation: The optimal subarray here is [2,4,5,6].

# Example 2:
# Input: nums = [5,2,1,2,5,2,1,2,5]
# Output: 8
# Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

# Constraints:
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104







from typing import List



# 2 pointer approach

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        seen = set() 
        curSum = 0
        maxSum = 0
        for right in range(len(nums)):
            if nums[right] in seen:
                while nums[left] != nums[right]:
                    curSum -= nums[left]
                    seen.remove(nums[left])
                    left += 1
                left += 1
            else:
                curSum += nums[right]
                seen.add(nums[right])
                right += 1
            maxSum = max(curSum, maxSum)
        return maxSum




# Same same but diffrent

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0
        seen = set()
        curSum = 0
        maxSum = 0

        for val in nums:
            while val in seen:
                seen.remove(nums[left])
                curSum -= nums[left]
                left += 1

            seen.add(val)
            curSum += val
            maxSum = max(maxSum, curSum)

        return maxSum
