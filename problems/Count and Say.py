# LeetCode Problem 38: Count and Say
# https://leetcode.com/problems/count-and-say/

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

# Given a positive integer n, return the nth element of the count-and-say sequence.

 

# Example 1:

# Input: n = 4

# Output: "1211"

# Explanation:

# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
# Example 2:

# Input: n = 1

# Output: "1"

# Explanation:

# This is the base case.

 

# Constraints:

# 1 <= n <= 30
 

# Follow up: Could you solve it iteratively?


# My classic approach idk the name...
# Beats 98% of the submissions


class Solution:
    def countAndSay(self, n: int) -> str:
        base = [1]
        for _ in range(n-1):
            temp = []
            cur = -1
            count = 0
            for c in base:
                if cur == c:
                    count += 1
                else:
                    if cur != -1:
                        temp.append(count)
                        temp.append(cur)
                    cur = c
                    count = 1

            temp.append(count)
            temp.append(cur)
            base = temp
        return ''.join(map(str, base))
    


# Let's try it in recursion

class Solution:
    def countAndSay(self, n: int) -> str:

        def rle(n,base):
            if n == 0: return ''.join(map(str, base))
            temp = []
            cur = -1
            count = 0
            for c in base:
                if cur == c:
                    count += 1
                else:
                    if cur != -1:
                        temp.append(count)
                        temp.append(cur)
                    cur = c
                    count = 1

            temp.append(count)
            temp.append(cur)
            return rle(n-1,temp)


        return "1" if n == 1 else rle(n-1,[1])
    



# Optimized version

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        return self._rle(prev)

    def _rle(self, s: str) -> str:
        res, count = [], 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                res.append(f"{count}{s[i - 1]}")
                count = 1
        res.append(f"{count}{s[-1]}")
        return "".join(res)
