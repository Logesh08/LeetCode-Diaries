# [869. Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/description/?envType=daily-question&envId=2025-08-10)

You are given an integer <code>n</code>. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return <code>true</code> if and only if we can do this so that the resulting number is a power of two.

**Example 1:** 

```
Input: n = 1
Output: true
```

**Example 2:** 

```
Input: n = 10
Output: false
```

**Constraints:** 

- <code>1 <= n <= 10^9</code>

---

## Solution

### My initial approach

```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = list(str(n))
        digits.sort()
        perms = []
        used = [False] * len(digits)

        def backtrack(path):
            if len(path) == len(digits):
                perms.append(path[:])
                return
            
            for i in range(len(digits)):
                if used[i] or (not path and digits[i] == '0'):
                    continue
                if i > 0 and digits[i] == digits[i-1] and not used[i-1]:
                    continue

                path.append(digits[i])
                used[i] = True

                backtrack(path)

                used[i] = False
                path.pop()



        backtrack([])

        for perm in perms:
            num = int(''.join(perm))
            if num > 0 and (num & (num - 1)) == 0:
                return True

        return False
```

### Optimzed variation

Just check if the sorted digits of `n` match the sorted digits of any power of 2 up to `2^30`.
It was so easy, my initial approach was overkill.
```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(str(n))
        for i in range(30):  # 2^30 is the largest power of 2 within the range of 10^9
            if sorted(str(1 << i)) == digits:
                return True
        return False
```