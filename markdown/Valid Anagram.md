# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)

Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1m:" data-state="closed" class="">anagram</button> of <code>s</code>, and <code>false</code> otherwise.

**Example 1:** 

<div class="example-block">
Input: s = "anagram", t = "nagaram"

Output: true

**Example 2:** 

<div class="example-block">
Input: s = "rat", t = "car"

Output: false

**Constraints:** 

- <code>1 <= s.length, t.length <= 5 * 10^4</code>
- <code>s</code> and <code>t</code> consist of lowercase English letters.

**Follow up:**  What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

---

### Solution in Python

```python
# Noob solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# God solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in set(s):
            if s.count(i) != t.count(i):
                return False
        return True
```