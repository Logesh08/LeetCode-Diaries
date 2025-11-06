# [287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/submissions/1822134377/)

Given an array of integers <code>nums</code> containing<code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.

There is only **one repeated number**  in <code>nums</code>, return thisrepeatednumber.

You must solve the problem **without**  modifying the array <code>nums</code>and using only constant extra space.

**Example 1:** 

```
Input: nums = [1,3,4,2,2]
Output: 2
```

**Example 2:** 

```
Input: nums = [3,1,3,4,2]
Output: 3
```

**Example 3:** 

```
Input: nums = [3,3,3,3,3]
Output: 3
```

**Constraints:** 

- <code>1 <= n <= 10^5</code>
- <code>nums.length == n + 1</code>
- <code>1 <= nums[i] <= n</code>
- All the integers in <code>nums</code> appear only **once**  except for **precisely one integer**  which appears **two or more**  times.

<b>Follow up:</b>

- How can we prove that at least one duplicate number must exist in <code>nums</code>?
- Can you solve the problem in linear runtime complexity?

---

## Solution

```python
# This is not standard case but this problem can be solved by Floyd's Algorithm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                # Fast and slow intersection point

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
                # Old and new slow intersection point
                # This is the place where the cycle begins
                # Cyble begins means, 2 or more nodes point to a same node
                # In this case for ex nums[i] = 2, nums[j] = 2, since both point here
                # This is where the cycle begins and the answer is also the same!

        return slow
```