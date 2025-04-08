# LeetCode Problem 416: Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
#
# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
#
# Example 1:
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
 

# Constraints:
# 1 <= nums.length <= 200
# 1 <= nums[i] <= 100



# While trying to solve this I realised something, If two subsets should be equal,
# It means subset1 + subset2 = FullList
# Also ValueOfSubset1 = ValueOfSubset2
# Which we can conclude as when two equal values are added, the result will always be even
# eg 3+3 => 6 which is even | eg 2+2 => which is even
# So It means that the sum of nums should always be even, if not it can be directly said as false



# This is my first approach which is greedy
# It passed 122/144 test cases
# But the thing is its wrong because we assume that both the subsets will be equal lenth
# But it can be possible that one subset is longer than the other
# for eg lhs can be [3,3,3] nd rhs can be [5,4]
# But definitely it can be used for equal lenth i guess

# Filed attempt


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target%2:
            return False

        lhs = rhs = 0
        for i in sorted(nums,reverse=True):
            if lhs > rhs:
                rhs += i
            else:
                lhs += i

        if lhs==rhs:
            return True

        return False


# This is my second approach using dynamic programming with set
# It passed all the test cases
# The time complexity is O(n*target) and space complexity is O(target)
# Runtime: 471 ms, beats 78.31%
# Wait just 78% seems like I should try to optimise it more or thats what I thought


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2:
            return False
        sums = {0}

        for i in nums:
            sums.update({ x+i for x in sums })
        
        return target//2 in sums
    

# Yooo, I just added an extra break condition and now I'm in top learderboard lol
# So this process is callled as pruning optimisation

# Runtime: 115 ms | beats 98.57%

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2:
            return False
        sums = {0}
        target //= 2

        for i in nums:
            sums.update({ x+i for x in sums })
            if target in sums: return True
        
        return False
    



# I have tried a solution using Knapsack DP approach, it's not optimal though...


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2:
            return False
        
        target //= 2

        dp = [False]*(target+1)
        dp[0] = True

        for num in nums:
            for i in range(target,num-1,-1):
                dp[i] = dp[i] or dp[i-num]
            if dp[target]: break

        return dp[target]