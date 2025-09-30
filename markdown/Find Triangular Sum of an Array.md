# [2221. Find Triangular Sum of an Array](https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30)

You are given a **0-indexed**  integer array <code>nums</code>, where <code>nums[i]</code> is a digit between <code>0</code> and <code>9</code> (**inclusive** ).

The **triangular sum**  of <code>nums</code> is the value of the only element present in <code>nums</code> after the following process terminates:

- Let <code>nums</code> comprise of <code>n</code> elements. If <code>n == 1</code>, **end**  the process. Otherwise, **create**  a new **0-indexed**  integer array <code>newNums</code> of length <code>n - 1</code>.
- For each index <code>i</code>, where <code>0 <= i <n - 1</code>, **assign**  the value of <code>newNums[i]</code> as <code>(nums[i] + nums[i+1]) % 10</code>, where <code>%</code> denotes modulo operator.
- **Replace**  the array <code>nums</code> with <code>newNums</code>.
- **Repeat**  the entire process starting from step 1.

Return the triangular sum of <code>nums</code>.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/22/ex1drawio.png" style="width: 250px; height: 250px;">

```
Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.```

**Example 2:** 

```
Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.```

**Constraints:** 

- <code>1 <= nums.length <= 1000</code>
- <code>0 <= nums[i] <= 9</code>

---

```python
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            for i in range(n-1, i-1, -1):
                nums[i] = (nums[i] + nums[i-1]) % 10
        return nums[n-1]
```