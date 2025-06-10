# LeetCode Problem 3442: Maximum Difference Between Even and Odd Frequency I
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/


# You are given a string s consisting of lowercase English letters.

# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.

 

# Example 1:

# Input: s = "aaaaabbc"

# Output: 3

# Explanation:

# The character 'a' has an odd frequency of 5, and 'b' has an even frequency of 2.
# The maximum difference is 5 - 2 = 3.
# Example 2:

# Input: s = "abcabcab"

# Output: 1

# Explanation:

# The character 'a' has an odd frequency of 3, and 'c' has an even frequency of 2.
# The maximum difference is 3 - 2 = 1.
 

# Constraints:

# 3 <= s.length <= 100
# s consists only of lowercase English letters.
# s contains at least one character with an odd frequency and one with an even frequency.






# In the question they are asking for the maximum diffrence, like the heigest value
# To obtain the height value, we can choose an odd lowest frequest (lF) and subtract
# it from the highest even freqency (hF) so that we may get the result.

# Let me try this approach

class Solution:
    def maxDifference(self, s: str) -> int:
        hef = -1
        hof = -1
        lef = 101
        lof = 101
        hashMap = {}
        for c in s:
            hashMap[c] = hashMap.get(c, 0) + 1
            if hashMap[c]%2:
                if hashMap[c] < lof:
                    lof = hashMap[c]
                if hashMap[c] > hof:
                    hof = hashMap[c]
            else:
                if hashMap[c] > hef:
                    hef = hashMap[c]
                if hashMap[c] < lef:
                    lef = hashMap[c]


        return max(hef - lof, hof - lef)
        # Failed program
    # Seems like i should have wait for the freqencices to update and complete then do the computation
    # It's clearly mentioned that we should subtract the even from the odd which i totally messed up!



# In this approach I've properly solved the issue

class Solution:
    def maxDifference(self, s: str) -> int:
        # First, count all frequencies
        hashMap = {}
        for c in s:
            hashMap[c] = hashMap.get(c, 0) + 1
        
        # Then find min/max for even and odd frequencies
        max_odd = -1
        min_even = float('inf')
        
        for freq in hashMap.values():
            if freq % 2 == 1:
                max_odd = max(max_odd, freq)
            else:
                min_even = min(min_even, freq)
        
        return max_odd - min_even