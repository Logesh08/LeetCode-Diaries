# LeetCode Problem 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.





# This is an important problem for me, because 4 years ago,
# In zoho campus Interview, I choose C and was not able to solve this
# IDK where I made a mistake but I was unable to solve it.

# Today I tried the same again and I done the program in the in the first try itself!!!
# Beats 100% of the submissions


class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        valids = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack:
                    top = stack.pop()
                else:
                    top = -1
                if top != valids[c]:
                    return False
                
        return not stack
