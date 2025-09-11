# [2785. Sort Vowels in a String](https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2025-09-11)

Given a **0-indexed**  string <code>s</code>, **permute**  <code>s</code> to get a new string <code>t</code> such that:

- All consonants remain in their original places. More formally, if there is an index <code>i</code> with <code>0 <= i < s.length</code> such that <code>s[i]</code> is a consonant, then <code>t[i] = s[i]</code>.
- The vowels must be sorted in the **nondecreasing**  order of their **ASCII**  values. More formally, for pairs of indices <code>i</code>, <code>j</code> with <code>0 <= i < j < s.length</code> such that <code>s[i]</code> and <code>s[j]</code> are vowels, then <code>t[i]</code> must not have a higher ASCII value than <code>t[j]</code>.

Return the resulting string.

The vowels are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>, and they can appear in lowercase or uppercase. Consonants comprise all letters that are not vowels.

**Example 1:** 

```
Input: s = "lEetcOde"
Output: "lEOtcede"
Explanation: 'E', 'O', and 'e' are the vowels in s; 'l', 't', 'c', and 'd' are all consonants. The vowels are sorted according to their ASCII values, and the consonants remain in the same places.
```

**Example 2:** 

```
Input: s = "lYmpH"
Output: "lYmpH"
Explanation: There are no vowels in s (all characters in s are consonants), so we return "lYmpH".
```

**Constraints:** 

- <code>1 <= s.length <= 10^5</code>
- <code>s</code> consists only of letters of theEnglish alphabetin **uppercase and lowercase** .

---

## Solution

```python
class Solution:
    def sortVowels(self, s: str) -> str:
        buffer = []
        ans = []

        for c in s:
            if c.lower() in "aeiou":
                ans.append(0)
                buffer.append(c)
            else:
                ans.append(c)

        buffer.sort(key= lambda x: ord(x))

        for i in range(len(s)-1,-1,-1):
            if ans[i] == 0:
                ans[i] = buffer.pop()

        return ''.join(ans)
```