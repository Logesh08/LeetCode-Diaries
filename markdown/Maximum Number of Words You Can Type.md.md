# [1935. Maximum Number of Words You Can Type](https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15)

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string <code>text</code> of words separated by a single space (no leading or trailing spaces) and a string <code>brokenLetters</code> of all **distinct**  letter keys that are broken, return the **number of words**  in <code>text</code> you can fully type using this keyboard.

**Example 1:** 

```
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
```

**Example 2:** 

```
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
```

**Example 3:** 

```
Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.
```

**Constraints:** 

- <code>1 <= text.length <= 10^4</code>
- <code>0 <= brokenLetters.length <= 26</code>
- <code>text</code> consists of words separated by a single space without any leading or trailing spaces.
- Each word only consists of lowercase English letters.
- <code>brokenLetters</code> consists of **distinct**  lowercase English letters.

---

## Solution

```python
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        ans = 0
        for word in text.split():
            canBeTyped  = True
            for char in brokenLetters:
                if char in word:
                    canBeTyped = False
                    break
            if canBeTyped:
                ans += 1
        return ans
```