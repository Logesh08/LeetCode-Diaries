# [1437. Check If All 1's Are at Least Length K Places Away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/?envType=daily-question&envId=2025-11-16)

Given an binary array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if all <code>1</code>'s are at least <code>k</code> places away from each other, otherwise return <code>false</code>.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png" style="width: 428px; height: 181px;">

```
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png" style="width: 320px; height: 173px;">

```
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
```

**Constraints:** 

- <code>1 <= nums.length <= 10^5</code>
- <code>0 <= k <= nums.length</code>
- <code>nums[i]</code> is <code>0</code> or <code>1</code>

---

## Solution

```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prevIndex = -k -1

        for i in range(len(nums)):
            if nums[i] == 1:
                if i - prevIndex -1 < k:
                    return False
                prevIndex = i
        
        return True
```