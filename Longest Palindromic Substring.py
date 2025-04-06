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
# But it is also O(n^3) time complexity

class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenght = len(s)
        for i in range(lenght):
            windowSize = lenght - i
            for j in range(lenght - windowSize + 1):
                subs = s[j:j+windowSize]
                if subs == subs[::-1]:
                    return subs
                


# Wow, I was finally able to understand a technique called "Expand Around Center"
# The idea is to expand around the center of the palindrome
# I thought is was not useful and expladnig around the center made no sense.. until I realised something..
# Everytime I have solved a problem with a palindrome, I use sliding window
# For eg, for str -> abcba, I generate all the substrings and check if they are palindromes
# so abcba -> a, b, c, b, a, ab, bc, cb, ba, abc, bcb, cba, abcb, abcba

# But when using the expand arround center tehcnique, I only considering substrings that are palindromes
# so abcba -> a, bcb and abcba ... only these 3 are palindromes are actually processed and we can cut down all the other substrings
# So the time complexity is O(n^2)
# Old one was O(n^3) because I was checking all the substrings and then checking if they are palindromes


# Runtime: 213ms | Beats 95.57%


class Solution:
    def longestPalindrome(self, s: str) -> str:
        total = len(s)
        maxLen = 0
        palStr = ''

        for i in range(total):

            # start with odd center
            oddPal = 1
            left = i-1
            right = i+1
            while left >= 0 and right < total:
                # sides available perform odd check
                if s[left] == s[right]:
                    oddPal += 2
                    left -= 1
                    right += 1
                else:
                    break
            
            if oddPal > maxLen:
                maxLen = oddPal
                palStr = s[left+1:right]


            # now even center
            evPal = 1
            left = i-1
            right = i+1
            if right < total and s[i] == s[right]:
                # found an even pair
                right += 1
                evPal = 2
                while left >= 0 and right < total:
                    if s[left] == s[right]:
                        evPal += 2
                        left -= 1
                        right += 1
                    else:
                        break
                    
            if evPal > maxLen:
                maxLen = evPal
                palStr = s[left+1:right]

        return palStr
    


# After reviewing with Ai, it suggested that I can remove oddPal and evPal variables
# It also suggested that I use a a single function, which I already thought about
# So here is the better one


class Solution:
    def longestPalindrome(self, s: str) -> str:            
        total = len(s)
        maxLen = 0
        palStr = ''

        def expandArroundCenter(left: int,right: int):
            nonlocal maxLen, palStr, total
            while left >= 0 and right < total and s[left] == s[right]:
                left -= 1
                right += 1
            
            palLen = right - left - 1
            if palLen > maxLen:
                maxLen = palLen
                palStr = s[left+1:right]

        
        for i in range(total):

            expandArroundCenter(i, i)
            expandArroundCenter(i, i+1)

        return 
    

# I came accross an algorithm called Manacher's algorithm
# It's said it just takes O(n) time complexity
# But I can't understand it for the last 3 days
# Finally I guess I understand 


# I guess it took me 3 days to understand Manacher's algorithm, because I was busy with other things
# This is my 21st submission
# Runtime: 52ms | Beats 97.22%

class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#'+'#'.join(s)+'#'
        p = [0] * len(t)
        c = r = 0

        for i in range(1,len(t)-1):
            
            mirror = c*2 - i

            if i < r:
                p[i] = min(p[mirror],r-i)

            while i-p[i]-1>=0 and i+p[i]+1<len(t) and t[i-p[i]-1]==t[i+p[i]+1]:
                p[i] += 1

            if i+p[i] > r:
                c = i
                r = i + p[i]

        radius = max(p)
        center = p.index(radius)
        start = (center - radius) // 2
        end = start + radius
        return s[start:end]