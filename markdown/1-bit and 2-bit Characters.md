# [717. 1-bit and 2-bit Characters](https://leetcode.com/problems/1-bit-and-2-bit-characters/description/?envType=daily-question&envId=2025-11-17)

We have two special characters:

- The first character can be represented by one bit <code>0</code>.
- The second character can be represented by two bits (<code>10</code> or <code>11</code>).

Given a binary array <code>bits</code> that ends with <code>0</code>, return <code>true</code> if the last character must be a one-bit character.

**Example 1:** 

```
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
```

**Example 2:** 

```
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
```

**Constraints:** 

- <code>1 <= bits.length <= 1000</code>
- <code>bits[i]</code> is either <code>0</code> or <code>1</code>.

---

## Solution

```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2

        return i == len(bits) - 1
```