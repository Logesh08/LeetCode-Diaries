# [3461. Check If Digits Are Equal in String After Operations I](https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/?envType=daily-question&envId=2025-10-21)

You are given a string <code>s</code> consisting of digits. Perform the following operation repeatedly until the string has **exactly**  two digits:

- For each pair of consecutive digits in <code>s</code>, starting from the first digit, calculate a new digit as the sum of the two digits **modulo**  10.
- Replace <code>s</code> with the sequence of newly calculated digits, maintaining the order in which they are computed.

Return <code>true</code> if the final two digits in <code>s</code> are the **same** ; otherwise, return <code>false</code>.

**Example 1:** 

<div class="example-block">
Input: s = "3902"

Output: true

Explanation:

- Initially, <code>s = "3902"</code>
- First operation:

- <code>(s[0] + s[1]) % 10 = (3 + 9) % 10 = 2</code>
- <code>(s[1] + s[2]) % 10 = (9 + 0) % 10 = 9</code>
- <code>(s[2] + s[3]) % 10 = (0 + 2) % 10 = 2</code>
- <code>s</code> becomes <code>"292"</code>

- Second operation:

- <code>(s[0] + s[1]) % 10 = (2 + 9) % 10 = 1</code>
- <code>(s[1] + s[2]) % 10 = (9 + 2) % 10 = 1</code>
- <code>s</code> becomes <code>"11"</code>

- Since the digits in <code>"11"</code> are the same, the output is <code>true</code>.

**Example 2:** 

<div class="example-block">
Input: s = "34789"

Output: false

Explanation:

- Initially, <code>s = "34789"</code>.
- After the first operation, <code>s = "7157"</code>.
- After the second operation, <code>s = "862"</code>.
- After the third operation, <code>s = "48"</code>.
- Since <code>'4' != '8'</code>, the output is <code>false</code>.

**Constraints:** 

- <code>3 <= s.length <= 100</code>
- <code>s</code> consists of only digits.

---

## Solution

```python
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [ord(ch) - 48 for ch in s]  # 5–10x faster than int() calls
        right = len(digits)
        while right > 2:
            for i in range(right-1):
                digits[i] = (digits[i] + digits[i+1]) % 10
            right -= 1
        return digits[0] == digits[1]
```