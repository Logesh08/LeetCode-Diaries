# LeetCode Problem 3201: Find the Maximum Length of Valid Subsequence I
# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/


# You are given an integer array nums.
# A subsequence sub of nums with length x is called valid if it satisfies:

# (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
# Return the length of the longest valid subsequence of nums.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

# Example 1:

# Input: nums = [1,2,3,4]

# Output: 4

# Explanation:

# The longest valid subsequence is [1, 2, 3, 4].

# Example 2:

# Input: nums = [1,2,1,1,2,1,2]

# Output: 6

# Explanation:

# The longest valid subsequence is [1, 2, 1, 2, 1, 2].

# Example 3:

# Input: nums = [1,3]

# Output: 2

# Explanation:

# The longest valid subsequence is [1, 3].

 

# Constraints:

# 2 <= nums.length <= 2 * 105
# 1 <= nums[i] <= 107




class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count_even = 0
        count_odd  = 0
        dp_even = 0
        dp_odd  = 0
    
        for x in nums:
            if x % 2 == 0:
                count_even += 1
                dp_even = max(dp_even, dp_odd + 1)
            else:
                count_odd += 1
                dp_odd  = max(dp_odd, dp_even + 1)
    
        same_parity_best = max(count_even, count_odd)
        alternating_best = max(dp_even, dp_odd)
    
        return max(same_parity_best, alternating_best)
