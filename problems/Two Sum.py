# LeetCode Problem 1: Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
# Approach:
# 1. Create a dictionary to store the indices of the numbers.
# 2. Iterate through the list of numbers.
# 3. For each number, calculate the complement (target - number).
# 4. Check if the complement is in the dictionary.
# 5. If it is, return the indices of the current number and the complement.
# 6. If it is not, add the current number and its index to the dictionary.
# 7. If no solution is found, return an empty list.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i,num in enumerate(nums):
            comp = target-num
            if comp in num_dict:
                return [num_dict[comp],i]
            num_dict[num] = i
        return []
    

# Learnt that dictionay can reduce the time complexity from O(n^2) to O(n)
# Also haven't used enumerate in a while
