# LeetCode Problem 2145: Count the Hidden Sequences
# https://leetcode.com/problems/count-the-hidden-sequences/


# You are given a 0-indexed array of n integers differences, 
# which describes the differences between each pair of 
# consecutive integers of a hidden sequence of length (n + 1). 
# More formally, call the hidden sequence hidden, 
# then we have that differences[i] = hidden[i + 1] - hidden[i].

# You are further given two integers lower and upper that describe 
# the inclusive range of values [lower, upper] that the hidden sequence can contain.

# For example, given differences = [1, -3, 4], lower = 1, upper = 6, 
# the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
# [3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
# [5, 6, 3, 7] is not possible since it contains an element greater than 6.
# [1, 2, 3, 4] is not possible since the differences are not correct.
# Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.

 


# Example 1:
# Input: differences = [1,-3,4], lower = 1, upper = 6
# Output: 2
# Explanation: The possible hidden sequences are:
# - [3, 4, 1, 5]
# - [4, 5, 2, 6]
# Thus, we return 2.

# Example 2:
# Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
# Output: 4
# Explanation: The possible hidden sequences are:
# - [-3, 0, -4, 1, 2, 0]
# - [-2, 1, -3, 2, 3, 1]
# - [-1, 2, -2, 3, 4, 2]
# - [0, 3, -1, 4, 5, 3]
# Thus, we return 4.

# Example 3:
# Input: differences = [4,-7,2], lower = 3, upper = 6
# Output: 0
# Explanation: There are no possible hidden sequences. Thus, we return 0.
 


# Constraints:
# n == differences.length
# 1 <= n <= 10^5
# -10^5 <= differences[i] <= 10^5
# -10^5 <= lower <= upper <= 10^5






# My elegant solution using prefix sum
# This question is just a puzzle of finding the range
# So correct upper with maxVal and lower with minVal

# The range is formulated based on:
# lower ≤ x + minVal        → x ≥ lower - minVal
# upper ≥ x + maxVal        → x ≤ upper - maxVal
# x ∈ [lower - minVal, upper - maxVal]
# (upper - maxVal) - (lower - minVal) + 1

# The solution is O(n) time complexity and O(1) space complexity

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        prefix = minVal = maxVal = lower

        for val in differences:
            prefix += val
            minVal = min(minVal,prefix)
            maxVal = max(maxVal,prefix)


        return max(0, upper - maxVal - lower + minVal + 1)
    




# Lets use accumalate to generate the prefix sum

# This is much faster than my approch

# Beats 98% of the submissions

from itertools import accumulate

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefixes = list(accumulate(differences, initial = lower))

        return max(0, upper - lower - max(prefixes) + min(prefixes) + 1)
    