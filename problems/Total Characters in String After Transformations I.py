# LeetCode Problem 3335: Total Characters in String After Transformations I
# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/


# You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

# If the character is 'z', replace it with the string "ab".
# Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
# Return the length of the resulting string after exactly t transformations.

# Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:

# Input: s = "abcyy", t = 2

# Output: 7

# Explanation:

# First Transformation (t = 1):
# 'a' becomes 'b'
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'y' becomes 'z'
# 'y' becomes 'z'
# String after the first transformation: "bcdzz"
# Second Transformation (t = 2):
# 'b' becomes 'c'
# 'c' becomes 'd'
# 'd' becomes 'e'
# 'z' becomes "ab"
# 'z' becomes "ab"
# String after the second transformation: "cdeabab"
# Final Length of the string: The string is "cdeabab", which has 7 characters.
# Example 2:

# Input: s = "azbk", t = 1

# Output: 5

# Explanation:

# First Transformation (t = 1):
# 'a' becomes 'b'
# 'z' becomes "ab"
# 'b' becomes 'c'
# 'k' becomes 'l'
# String after the first transformation: "babcl"
# Final Length of the string: The string is "babcl", which has 5 characters.
 

# Constraints:

# 1 <= s.length <= 10^5
# s consists only of lowercase English letters.
# 1 <= t <= 10^5




# This approach is solid and great memory wise

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        chars = [0] * 26

        for ch in s:
            chars[ord(ch) - ord('a')] += 1


        for _ in range(t):
            temp = [0] * 26
            for i in range(25):
                temp[i+1] = chars[i]
            temp[0] = chars[25]
            temp[1] += chars[25]
            chars = temp


        return sum(chars) % MOD
            




# Beats 90% in time complexity

from collections import deque

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        data = deque([0] * 26)

        for ch in s:
            data[ord(ch) - 97] += 1

        for _ in range(t):
            z = data.pop()
            data[0] += z
            data.appendleft(z)

        return sum(data) % MOD
    



# This dp approach beats 100% of the submissions

from collections import Counter

dp = [1] * (100_000 + 26)
for i in range(26, len(dp)):
    dp[i] = (dp[i-26] + dp[i-25]) % 1_000_000_007

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ans = 0
        cnt = Counter(s)
        for k, v in cnt.items():
            ans = (ans + v * dp[(ord(k) - 97) + t]) % 1_000_000_007
        return ans
    


# A notable approach because the use of @cache is detected

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        ans = 0
        for c in s:
            i = ord(c) - ord('a')
            ans += val(t+i)
        return ans % (10**9 + 7)

@cache
def val(c):
    if c >= 26:
        return val(c-26) + val(c+1-26)
    return 1
        