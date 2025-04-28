# LeetCode Problem 2302: Count Subarrays With Score Less Than K
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/


# The score of an array is defined as the product of its sum and its length.

# For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
# Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

# A subarray is a contiguous sequence of elements within an array.

 

# Example 1:

# Input: nums = [2,1,4,3,5], k = 10
# Output: 6
# Explanation:
# The 6 subarrays having scores less than 10 are:
# - [2] with score 2 * 1 = 2.
# - [1] with score 1 * 1 = 1.
# - [4] with score 4 * 1 = 4.
# - [3] with score 3 * 1 = 3. 
# - [5] with score 5 * 1 = 5.
# - [2,1] with score (2 + 1) * 2 = 6.
# Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.
# Example 2:

# Input: nums = [1,1,1], k = 5
# Output: 5
# Explanation:
# Every subarray except [1,1,1] has a score less than 5.
# [1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
# Thus, there are 5 subarrays having scores less than 5.
 

# Constraints:

# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^15




# Ahh my sweet first Attempt Submission failed,
# I thought maybe it will work, even though seeing the constrains

# 152 / 167 testcases passed
# Got TLE

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = 0

        for i in range(n):
            sum = 0
            cur_len = 0
            for j in range(i,n):
                cur_len += 1
                sum += nums[j]
                if sum * cur_len < k:
                    ans += 1
                else:
                    break

        return ans
    


# Imma try using a single for loop

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = 0
        left = 0
        cur_sum = 0

        for right in range(n):
            cur_len = right - left + 1
            cur_sum += nums[right]

            while cur_len * cur_sum >= k and left <= right:
                cur_sum -= nums[left]
                left += 1
                cur_len -= 1

            if cur_len * cur_sum < k:
                ans += cur_len 
                
        return ans
    


# I just removed the if condition and added the cur_len to ans
# Because the while loop will always make sure 
# that the cur_len * cur_sum is less than k



class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        ans = 0
        left = 0
        cur_sum = 0

        for right in range(n):
            cur_len = right - left + 1
            cur_sum += nums[right]

            while cur_len * cur_sum >= k and left <= right:
                cur_sum -= nums[left]
                left += 1
                cur_len -= 1

            # if cur_len * cur_sum < k:
            ans += cur_len 

        return ans