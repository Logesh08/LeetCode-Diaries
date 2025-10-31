# [3289. The Two Sneaky Numbers of Digitville](https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=daily-question&envId=2025-10-29)

In the town of Digitville, there was a list of numbers called <code>nums</code> containing integers from <code>0</code> to <code>n - 1</code>. Each number was supposed to appear **exactly once**  in the list, however, **two**  mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size **two**  containing the two numbers (in any order), so peace can return to Digitville.

**Example 1:** 

<div class="example-block">
Input: nums = [0,1,1,0]

Output: [0,1]

Explanation:

The numbers 0 and 1 each appear twice in the array.

**Example 2:** 

<div class="example-block">
Input: nums = [0,3,2,1,3,2]

Output: [2,3]

Explanation: 

The numbers 2 and 3 each appear twice in the array.

**Example 3:** 

<div class="example-block">
Input: nums = [7,1,5,4,3,4,6,0,9,5,8,2]

Output: [4,5]

Explanation: 

The numbers 4 and 5 each appear twice in the array.

**Constraints:** 

<li data-stringify-border="0" data-stringify-indent="1"><code>2 <= n <= 100</code>
<li data-stringify-border="0" data-stringify-indent="1"><code>nums.length == n + 2</code>
<li data-stringify-border="0" data-stringify-indent="1"><code data-stringify-type="code">0 <= nums[i] < n</code>
<li data-stringify-border="0" data-stringify-indent="1">The input is generated such that <code>nums</code> contains **exactly**  two repeated elements.

---

## Solution

```python
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hashSet = set()
        ans = []
        for num in nums:
            if num in hashSet:
                ans.append(num)
            else:
                hashSet.add(num)
        return ans
```