# Leetcode Problem 2234: Count Symmetric Integers
# https://leetcode.com/problems/count-symmetric-integers/



# You are given two positive integers low and high.

# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

# Return the number of symmetric integers in the range [low, high].

 


# Example 1:
# Input: low = 1, high = 100
# Output: 9
# Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

# Example 2:
# Input: low = 1200, high = 1230
# Output: 4
# Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
 


# Constraints:
# 1 <= low <= high <= 10^4



# I solved the problem using brute force I gueess.
# It's o(n) and it worked only because the range is small. [10^4]
# I will think of other ways to solve the problem.



class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        if high<10: return 0
        si = 0
        for i in range(low,high+1):
            s = str(i)
            l = len(s)//2
            if sum(list(map(int,str(i)[:l + l%2]))) == sum(list(map(int,str(i)[l:]))):
                si += 1
        
        return si
    

# We can do it without list
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        si = 0
        for i in range(low,high+1):
            s = str(i)
            l = len(s)
            if len(s)%2: continue
            if sum(map(int,str(i)[:l//2])) == sum(map(int,str(i)[l//2:])):
                si += 1
        
        return si
    




# This is enumaration approach were we explicitly use the number between (10 and 199) then (1000 and 9999)
# The solution is correct and works for the given constraints.
# O(high - low) time complexity

# Runtime: 102ms | Beats 97.56% of submissions


class Solution(object):
    def countSymmetricIntegers(self, low, high):
        ans = 0
        for i in range(low, high + 1):
            if i < 100 and i % 11 == 0:
                ans += 1 
            elif 1000 <= i < 10000:
                left = i // 1000 + (i//100 % 10) 
                right = (i//10 % 10)  + i % 10
                if left == right:
                    ans += 1
        return ans



