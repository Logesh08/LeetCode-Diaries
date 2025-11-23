# [1262. Greatest Sum Divisible by Three](https://leetcode.com/problems/greatest-sum-divisible-by-three/description/?envType=daily-question&envId=2025-11-22)

Given an integer array <code>nums</code>, return the **maximum possible sum ** of elements of the array such that it is divisible by three.

**Example 1:** 

```
Input: nums = [3,6,5,1,8]
Output: 18
Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum divisible by 3).
```

**Example 2:** 

```
Input: nums = [4]
Output: 0
Explanation: Since 4 is not divisible by 3, do not pick any number.
```

**Example 3:** 

```
Input: nums = [1,2,3,4,4]
Output: 12
Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum divisible by 3).
```

**Constraints:** 

- <code>1 <= nums.length <= 4 * 10^4</code>
- <code>1 <= nums[i] <= 10^4</code>

---

## Solution

```python
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = 0
        smallestOnes = float("inf")
        smallestTwos = float("inf")


        for num in nums:
            if num % 3 == 1:
                smallestTwos = min(smallestTwos, num + smallestOnes)
                smallestOnes = min(smallestOnes, num)
            elif num % 3 == 2:
                smallestOnes = min(smallestOnes, num + smallestTwos)
                smallestTwos = min(smallestTwos, num)


            total += num

        if total % 3 == 0:
            return total
        if total % 3 == 1:
            return total - smallestOnes
        if total % 3 == 2:
            return total - smallestTwos
```