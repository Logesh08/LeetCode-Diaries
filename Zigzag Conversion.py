# LeetCode Problem 6: Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# Example 3:

# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000



# This is my first solution, I tired hard to solve in O(n)
# Idk if its a good way or not...

# It beats only 42.55% of submissions..
# It feels like I have missed something

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        if numRows==1: return s
        ans=''
        base = (numRows-1) * 2
        for i in range(numRows):
            for cur in range(i,n,base):
                ans += s[cur]
                right = cur + base - i*2
                if i>0 and i<numRows-1 and right < n:
                    ans += s[right]

        return ans



# Yo yoo crazyyy stuff happend, I just switched to list and BOOM!
# It beats 93.63% of the submissions..
# Guess my first solution was not that bad after all
# TimeComplexity: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n=len(s)
        if numRows==1: return s
        ans=[]
        base = (numRows-1) * 2
        for i in range(numRows):
            for cur in range(i,n,base):
                ans.append(s[cur])
                right = cur + base - i*2
                if i>0 and i<numRows-1 and right < n:
                    ans.append(s[right])

        return ''.join(ans)
