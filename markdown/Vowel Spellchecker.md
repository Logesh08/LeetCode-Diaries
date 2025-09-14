# [966. Vowel Spellchecker](https://leetcode.com/problems/vowel-spellchecker/description/?envType=daily-question&envId=2025-09-14)

Given a <code>wordlist</code>, we want to implement a spellchecker that converts a query word into a correct word.

For a given <code>query</code> word, the spell checker handles two categories of spelling mistakes:

- Capitalization: If the query matches a word in the wordlist (**case-insensitive** ), then the query word is returned with the same case as the case in the wordlist.

- Example: <code>wordlist = ["yellow"]</code>, <code>query = "YellOw"</code>: <code>correct = "yellow"</code>
- Example: <code>wordlist = ["Yellow"]</code>, <code>query = "yellow"</code>: <code>correct = "Yellow"</code>
- Example: <code>wordlist = ["yellow"]</code>, <code>query = "yellow"</code>: <code>correct = "yellow"</code>

- Vowel Errors: If after replacing the vowels <code>('a', 'e', 'i', 'o', 'u')</code> of the query word with any vowel individually, it matches a word in the wordlist (**case-insensitive** ), then the query word is returned with the same case as the match in the wordlist.

- Example: <code>wordlist = ["YellOw"]</code>, <code>query = "yollow"</code>: <code>correct = "YellOw"</code>
- Example: <code>wordlist = ["YellOw"]</code>, <code>query = "yeellow"</code>: <code>correct = ""</code> (no match)
- Example: <code>wordlist = ["YellOw"]</code>, <code>query = "yllw"</code>: <code>correct = ""</code> (no match)

In addition, the spell checker operates under the following precedence rules:

- When the query exactly matches a word in the wordlist (**case-sensitive** ), you should return the same word back.
- When the query matches a word up to capitlization, you should return the first such match in the wordlist.
- When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
- If the query has no matches in the wordlist, you should return the empty string.

Given some <code>queries</code>, return a list of words <code>answer</code>, where <code>answer[i]</code> is the correct word for <code>query = queries[i]</code>.

**Example 1:** 

```
Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```

**Example 2:** 

```
Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]
```

**Constraints:** 

- <code>1 <= wordlist.length, queries.length <= 5000</code>
- <code>1 <= wordlist[i].length, queries[i].length <= 7</code>
- <code>wordlist[i]</code> and <code>queries[i]</code> consist only of only English letters.

---

## Solution

```python
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def case_hash(s):
            return s.lower()
        
        def vowel_hash(s):
            return s.lower().replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')
        
        
        exact = set(wordlist)
        case = defaultdict()
        vowl = defaultdict()
        for w in wordlist:
            c = case_hash(w)
            if c not in case: case[c] = w
            v = vowel_hash(w)
            if v not in vowl: vowl[v] = w
        
        def correct(w):
            if w in exact: return w
            c = case_hash(w)
            if c in case: return case[c]
            v = vowel_hash(w)
            if v in vowl: return vowl[v]
            return ''
                    
        return [correct(q) for q in queries]
```