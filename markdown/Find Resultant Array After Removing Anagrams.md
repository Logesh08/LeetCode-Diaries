# [2273. Find Resultant Array After Removing Anagrams](https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-11)

You are given a **0-indexed**  string array <code>words</code>, where <code>words[i]</code> consists of lowercase English letters.

In one operation, select any index <code>i</code> such that <code>0 < i < words.length</code> and <code>words[i - 1]</code> and <code>words[i]</code> are **anagrams** , and **delete**  <code>words[i]</code> from <code>words</code>. Keep performing this operation as long as you can select an index that satisfies the conditions.

Return <code>words</code> after performing all operations. It can be shown that selecting the indices for each operation in **any**  arbitrary order will lead to the same result.

An **Anagram**  is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, <code>"dacb"</code> is an anagram of <code>"abdc"</code>.

**Example 1:** 

```
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Explanation:
One of the ways we can obtain the resultant array is by using the following operations:
- Since words[2] = "bbaa" and words[1] = "baba" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","baba","cd","cd"].
- Since words[1] = "baba" and words[0] = "abba" are anagrams, we choose index 1 and delete words[1].
  Now words = ["abba","cd","cd"].
- Since words[2] = "cd" and words[1] = "cd" are anagrams, we choose index 2 and delete words[2].
  Now words = ["abba","cd"].
We can no longer perform any operations, so ["abba","cd"] is the final answer.```

**Example 2:** 

```
Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]
Explanation:
No two adjacent strings in words are anagrams of each other, so no operations are performed.```

**Constraints:** 

- <code>1 <= words.length <= 100</code>
- <code>1 <= words[i].length <= 10</code>
- <code>words[i]</code> consists of lowercase English letters.

---

## Solution

```python
class Solution(object):
    def removeAnagrams(self, words):
        ans = [words[0]]
        for i in range(1, len(words)):
            a, b = sorted(words[i]), sorted(ans[-1])
            if a != b:
                ans.append(words[i])
        return ans
```