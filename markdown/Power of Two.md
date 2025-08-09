# [231. Power of Two](https://leetcode.com/problems/power-of-two/description/?envType=daily-question&envId=2025-08-09)

Given an integer <code>n</code>, return <code>true</code> if it is a power of two. Otherwise, return <code>false</code>.

An integer <code>n</code> is a power of two, if there exists an integer <code>x</code> such that <code>n == 2^x</code>.

**Example 1:** 

```
Input: n = 1
Output: true
Explanation: 2^0 = 1
```

**Example 2:** 

```
Input: n = 16
Output: true
Explanation: 2^4 = 16
```

**Example 3:** 

```
Input: n = 3
Output: false
```

**Constraints:** 

- <code>-2^31 <= n <= 2^31 - 1</code>

**Follow up:**  Could you solve it without loops/recursion?

---

## Solutions

### 1. Loop (Repeated Division)
Keep dividing by 2 while it is divisible. If you land exactly on 1 it is a power of two.
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
```
Time: O(log n)  |  Space: O(1)

### 2. Bit Trick (Best / Follow‑up, no loops needed conceptually)
A positive power of two has exactly one set bit. Clearing the lowest set bit with (n & (n-1)) yields 0 only for powers of two.
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
```
Time: O(1)  |  Space: O(1)

### 3. Use Highest Power Within 32-bit Signed Range
Largest 2^k within 32-bit signed range is 2^30 = 1_073_741_824. Every positive power of two divides it.
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and 1_073_741_824 % n == 0
```
Time: O(1)  |  Space: O(1)

### 4. Bit Count (Python 3.8+)
Exactly one bit set means bit_count() == 1.
```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n.bit_count() == 1
```
Time: O(1)  |  Space: O(1)