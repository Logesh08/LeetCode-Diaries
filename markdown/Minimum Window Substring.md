# [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)

Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and <code>n</code> respectively, return the **minimum window**  <button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:r1k:" data-state="closed" class="">**substring** </button> of <code>s</code> such that every character in <code>t</code> (**including duplicates** ) is included in the window. If there is no such substring, return the empty string <code>""</code>.

The testcases will be generated such that the answer is **unique** .

**Example 1:** 

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
```

**Example 2:** 

```
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
```

**Example 3:** 

```
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
```

**Constraints:** 

- <code>m == s.length</code>
- <code>n == t.length</code>
- <code>1 <= m, n <= 10^5</code>
- <code>s</code> and <code>t</code> consist of uppercase and lowercase English letters.

**Follow up:**  Could you find an algorithm that runs in <code>O(m + n)</code> time?

---

## Solution

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        window = {}

        for ch in t:
            target[ch] = target.get(ch, 0) + 1

        need = len(target)
        have = 0

        start = end = -1
        minLen = float("inf")

        left = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in target:
                window[ch] = window.get(ch, 0) + 1
            
                if window[ch] == target[ch]:
                    have += 1

            while have == need:
                if (right - left + 1) < minLen:
                    start = left
                    end = right
                    minLen = right - left + 1
                ch = s[left]
                if ch in window:
                    window[ch] -= 1
                    if window[ch] == target[ch] - 1:
                        have -= 1
                left += 1
                

        return s[start:end+1] if minLen != float("inf") else ""
```