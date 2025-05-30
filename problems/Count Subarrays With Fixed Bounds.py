# You are given an integer array nums and two integers minK and maxK.

# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.

# A subarray is a contiguous part of an array.



# Example 1:
# Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
# Output: 2
# Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].

# Example 2:
# Input: nums = [1,1,1,1], minK = 1, maxK = 1
# Output: 10
# Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.



# Constraints:

# 2 <= nums.length <= 10^5
# 1 <= nums[i], minK, maxK <= 10^6




# This is a solution I though of by using only valid subsets
# for each subset, I have to find and increment the count

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        subArrays = []
        temp = []
        for i in range(n):
            val = nums[i]
            if val >= minK and val <= maxK:
                temp.append(val)
            else:
                if temp:
                    subArrays.append(temp)
                    temp = []
        subArrays.append(temp)

        count = 0
        for subArray in subArrays:
            if len(subArray) == 0:
                continue
            minIndex = -1
            maxIndex = -1
            for i in range(len(subArray)):
                if subArray[i] == minK:
                    minIndex = i
                if subArray[i] == maxK:
                    maxIndex = i
                if minIndex != -1 and maxIndex != -1:
                    count += min(minIndex, maxIndex) + 1
        return count
    


# Actually we can implement the above logic in a simpler way


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        badIndex = currMin = currMax = -1
        res = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                badIndex = i
            if num == minK:
                currMin = i
            if num == maxK:
                currMax = i
            res += max(0, min(currMin, currMax) - badIndex)
        return res
    


# This version improves performance drastically!    

class Solution:
    def countSubarrays(self, nums: List[int], min_k: int, max_k: int) -> int:
        ans = 0
        min_i = max_i = i0 = -1
        for i, x in enumerate(nums):
            if x == min_k: min_i = i
            if x == max_k: max_i = i
            if not min_k <= x <= max_k: i0 = i
            j = min_i if min_i < max_i else max_i
            if j > i0: ans += j - i0
        return ans