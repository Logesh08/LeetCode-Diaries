# LeetCode Problem 3272: Find the Count of Good Integers
# https://leetcode.com/problems/find-the-count-of-good-integers/



# You are given two positive integers n and k.

# An integer x is called k-palindromic if:

# x is a palindrome.
# x is divisible by k.
# An integer is called good if its digits can be rearranged to form a k-palindromic integer. For example, for k = 2, 2020 can be rearranged to form the k-palindromic integer 2002, whereas 1010 cannot be rearranged to form a k-palindromic integer.

# Return the count of good integers containing n digits.

# Note that any integer must not have leading zeros, neither before nor after rearrangement. For example, 1010 cannot be rearranged to form 101.

 

# Example 1:

# Input: n = 3, k = 5

# Output: 27

# Explanation:

# Some of the good integers are:

# 551 because it can be rearranged to form 515.
# 525 because it is already k-palindromic.
# Example 2:

# Input: n = 1, k = 4

# Output: 2

# Explanation:

# The two good integers are 4 and 8.

# Example 3:

# Input: n = 5, k = 6

# Output: 2468

 

# Constraints:

# 1 <= n <= 10
# 1 <= k <= 9




# Solution using pure maths
# Instead of looping each number and trying to generate possibilies, we can first check all the palindromic numbers only
# And we can then just focus on the permutation of the digits


# I need to redo these kinda problems again

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        hashMap = set()
        half = (n+1) // 2
        start = 10 ** (half-1)
        end = 10 ** half

        for i in range(start, end):
            s = str(i)
            if n%2:
                num = s + s[:-1][::-1]
            else:
                num = s + s[::-1]

            if int(num)%k == 0:
                hashMap.add(''.join(sorted(num)))

        facts = [1] * (n+1)
        for i in range(1, n+1):
            facts[i] = facts[i-1] * i


        ans = 0
        for s in hashMap:
            freq = [0]*10
            for c in s:
                freq[int(c)] += 1

            perms = 0

            for d in range(1,10):
                if freq[d] == 0:
                    continue

                freq[d] -= 1
                p = facts[n-1]

                for c in freq:
                    p //= facts[c]

                perms += p
                freq[d] += 1

            ans += perms

        return ans




# This is a funny solution I found in the web using Lookup table

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        return ([
            [9, 9, 243, 252, 10935, 10944, 617463, 617472, 41457015, 41457024],
            [4, 4, 108, 172, 7400, 9064, 509248, 563392, 37728000, 39718144],
            [3, 3, 69, 84, 3573, 3744, 206217, 207840, 13726509, 13831104],
            [2, 2, 54, 98, 4208, 6992, 393948, 494818, 33175696, 37326452],
            [1, 1, 27, 52, 2231, 3256, 182335, 237112, 15814071, 19284856],
            [1, 1, 30, 58, 2468, 3109, 170176, 188945, 12476696, 13249798],
            [1, 1, 33, 76, 2665, 3044, 377610, 506388, 36789447, 40242031],
            [1, 1, 27, 52, 2231, 5221, 292692, 460048, 30771543, 35755906],
            [1, 1, 23, 28, 1191, 1248, 68739, 69280, 4623119, 4610368]
        ])[k - 1][n - 1]