# [1323. Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/description/?envType=daily-question&envId=2025-08-16)

You are given a positive integer <code>num</code> consisting only of digits <code>6</code> and <code>9</code>.

Return the maximum number you can get by changing **at most**  one digit (<code>6</code> becomes <code>9</code>, and <code>9</code> becomes <code>6</code>).

**Example 1:** 

```
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
```

**Example 2:** 

```
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
```

**Example 3:** 

```
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
```

**Constraints:** 

- <code>1 <= num <= 10^4</code>
- <code>num</code>consists of only <code>6</code> and <code>9</code> digits.

---

## Solution

```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        digit_list = list(str(num))
        for i in range(len(digit_list)):
            if digit_list[i] == '6':
                digit_list[i] = '9'
                return int(''.join(digit_list))
        return num
```

```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        num = num.replace('6', '9', 1)
        return int(num)
```

Pure numeric approach:

```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        pos = -1  # to store position of leftmost 6
        i = 0     # digit index from right (0 = ones place)

        while n > 0:
            digit = n % 10
            if digit == 6:
                pos = i  # update position of last seen 6
            n //= 10
            i += 1

        if pos == -1:  # no 6 found
            return num
        return num + 3 * (10 ** pos)
```