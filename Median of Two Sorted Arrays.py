# LeetCode Problem 4: Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6

# This is my solution, but it is O((m+n)log(m+n)) time complexity

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = sorted(nums1 + nums2)
        len_x = len(x)
        return x[len_x//2] if len_x%2 else (x[len_x//2 - 1] + x[len_x//2])/2
    

# This is my optimal solution with O(log(min(m,n))) time complexity
# Funfact: Target was to acheive just O(log(m+n)) but I ended up with O(log(min(m,n)))
# It took me two days to find how to properly implement the binary search
# Runtime: Beats 100% of submissions    | O(log(min(m,n)))
# Memorry: Beats 84.07% of submissions  | O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1,len2 = len(nums1),len(nums2)
        full = len1+len2
        half = full//2

        left,right = 0,len1

        while True:
            p1 = (left + right) // 2
            p2 = half - p1

            left1 = nums1[p1-1] if p1 > 0 else float("-inf")
            right1 = nums1[p1] if p1 < len1 else float("inf")

            left2 = nums2[p2-1] if p2 > 0 else float("-inf")
            right2 = nums2[p2] if p2 < len2 else float("inf")

            if left1<=right2 and left2<=right1:
                if full%2:
                    return min(right1,right2)
                return (max(left1,left2)+min(right1,right2))/2
                    
            if left1 > right2:
                right = p1 - 1 
            else:
                left = p1 + 1




