# LeetCode Problem 5: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
#
# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.


# This is my initial solution, but it is O(n^3) time complexity
# Wopping 9173ms runtime, so lets see if we can make it better

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenght = len(s)
        longest = ""
        for i in range(lenght):
            for j in range(i+1,lenght+1):
                subs = s[i:j]
                if subs == subs[::-1] and len(longest)<len(subs):
                    longest = subs
        return longest
    

# Well, if we start from the biggest substring there is no need to check the smaller ones
# So we can just return the first one we find
# But still its not the best

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenght = len(s)
        for i in range(lenght):
            windowSize = lenght - i
            for j in range(lenght - windowSize + 1):
                subs = s[j:j+windowSize]
                if subs == subs[::-1]:
                    return subs