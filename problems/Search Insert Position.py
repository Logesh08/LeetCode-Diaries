# LeetCode Problem 35: Search Insert Position
# https://leetcode.com/problems/search-insert-position/


# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 10^4
# -104 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 10^4







# We can notice that they are asking for a solution 
# in O(log n), which means it's a binary search


# Beats 100% of the submisssions

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start < end:

            mid = (start+end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start + 1