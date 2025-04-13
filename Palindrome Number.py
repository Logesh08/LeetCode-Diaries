# LeetCode Problem 9: Palindrome Number
# https://leetcode.com/problems/palindrome-number/

# Given an integer x, return true if x is a palindrome, and false otherwise.



# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


# Constraints:
# -2^31 <= x <= 2^31 - 1

# Follow up: Could you solve it without converting the integer to a string?


# Classic python solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
    
# Two pointer approach
class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = str(x)
        length = len(new_x) - 1
        for i in range(length//2+1):
            if new_x[i] != new_x[length - i]:
                return False
        return True
    

# Okay lets try to do without sting...
# But 2^32 sounds scary

class Solution:
    def isPalindrome(self, x: int) -> bool:
        new = 0
        temp = x
        
        while temp > 0:
            new *= 10
            new += temp%10
            temp //= 10

        return new == x
    

# Lol the classic way itself works fine