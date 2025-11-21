

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = {s[0]}
        right = {}

        for i in range(1, len(s)):
            right[s[i]] = right.get(s[i], 0) + 1

        res = set()

        for i in range(len(s)):
            right[s[i]] += 1
            for c in left:
                if right.get(c, 0) > 0:
                    res.add((c, s[i]))
            left.add(s[i])

        return len(res)