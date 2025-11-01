from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        # Swapping so that we perform binary search on the minimum length of the list

        full = n + m
        half = full // 2

        left, right = 0, n - 1

        while True:
            midOf1 = left + (right - left) // 2 # Std binary search
            midOf2 = half - midOf1 - 2          # Hlaf - midOf1 -> is remaining partition length, but we need to sub -1 two times(-2)
                                                                                            # Cuz full is size of 2 zero index lists        
            left1 = nums1[midOf1] if midOf1 > -1 else float("-inf")
            right1 = nums1[midOf1+1] if midOf1+1 < n else float("inf")
            left2 = nums2[midOf2] if midOf2 > -1 else float("-inf")
            right2 = nums2[midOf2+1] if midOf2+1 < m else float("inf")
            # We make partitions and assing infinities if the partion excceeds the boundary

            if left1 <= right2 and left2 <= right1:
                if full % 2:                        # When the len is odd, there is an extra element on the right side
                    return min(right1, right2)      # that's why we take min of right and not max left
                return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = midOf1 - 1
            else:
                left = midOf1 + 1