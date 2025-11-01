# [4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)

Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size <code>m</code> and <code>n</code> respectively, return **the median**  of the two sorted arrays.

The overall run time complexity should be <code>O(log (m+n))</code>.

**Example 1:** 

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

**Example 2:** 

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

**Constraints:** 

- <code>nums1.length == m</code>
- <code>nums2.length == n</code>
- <code>0 <= m <= 1000</code>
- <code>0 <= n <= 1000</code>
- <code>1 <= m + n <= 2000</code>
- <code>-10^6 <= nums1[i], nums2[i] <= 10^6</code>

---

## Solution
```python
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
```