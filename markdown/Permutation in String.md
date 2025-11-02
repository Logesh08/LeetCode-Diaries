# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)

Given two strings <code>s1</code> and <code>s2</code>, return <code>true</code> if <code>s2</code> contains a <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1k:" data-state="closed" class="">permutation</button> of <code>s1</code>, or <code>false</code> otherwise.

In other words, return <code>true</code> if one of <code>s1</code>'s permutations is the substring of <code>s2</code>.

**Example 1:** 

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
```

**Example 2:** 

```
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
```

**Constraints:** 

- <code>1 <= s1.length, s2.length <= 10^4</code>
- <code>s1</code> and <code>s2</code> consist of lowercase English letters.

---

## Solution

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[right]) - ord('a')
            s2Count[index] += 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] + 1:
                matches -= 1

            index = ord(s2[left]) - ord('a')
            s2Count[index] -= 1
            if s2Count[index] == s1Count[index]:
                matches += 1
            elif s2Count[index] == s1Count[index] - 1:
                matches -= 1

            left += 1
        return matches == 26
```