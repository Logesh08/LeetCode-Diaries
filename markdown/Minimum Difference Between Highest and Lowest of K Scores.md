# [1984. Minimum Difference Between Highest and Lowest of K Scores](https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/?envType=daily-question&envId=2026-01-25)

You are given a **0-indexed**  integer array <code>nums</code>, where <code>nums[i]</code> represents the score of the <code>i^th</code> student. You are also given an integer <code>k</code>.

Pick the scores of any <code>k</code> students from the array so that the **difference**  between the **highest**  and the **lowest**  of the <code>k</code> scores is **minimized** .

Return the **minimum**  possible difference.

**Example 1:** 

```
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [**90** ]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.
```

**Example 2:** 

```
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [**9** ,**4** ,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [**9** ,4,**1** ,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [**9** ,4,1,**7** ]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,**4** ,**1** ,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,**4** ,1,**7** ]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,**1** ,**7** ]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
```

**Constraints:** 

- <code>1 <= k <= nums.length <= 1000</code>
- <code>0 <= nums[i] <= 10^5</code>

---

## Solution

```python
class Solution:
    def minimumDifference(self, nums, k):
        n = len(nums)
        nums.sort()
        ans = nums[k - 1] - nums[0]
        for i in range(0, n - k + 1):
            if nums[i + k - 1] - nums[i] < ans:
                ans = nums[i + k - 1] - nums[i]
        return ans
```