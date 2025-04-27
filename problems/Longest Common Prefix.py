# LeetCode Problem 14: Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/


# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.




# I dont have any idea of how to do this, 
# First let's try un-optimized approach of O(n * min([len(s) for s in strs])) 

# Well turns out its a good solution, not bad as I thought!
# LOL, I ran it a few times and It beat 
# Beats 100% of the submissions and runs in 0 ms
# Memory wise beats 96.03% 


# Demn, sometimes I guess we can only do things like this!

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        minLen = min([len(s) for s in strs])

        for i in range(minLen):
            flag = False
            for str in strs:
                if str[i] != strs[0][i]:
                    flag = True
                    break
            if flag:
                break
            ans.append(strs[0][i])
            

        return ''.join(ans)