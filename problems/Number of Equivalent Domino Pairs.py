# LeetCode Problem 1128: Number of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/


# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

# Example 1:

# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:

# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
 

# Constraints:

# 1 <= dominoes.length <= 4 * 10^4
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9






# My first solution, works but for one test case it gets TLE
# TLE error
# Time complexity: O(n^2)


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        n = len(dominoes)

        ans = 0

        for i in range(n):
            for j in range(i+1,n):
                if dominoes[i] == dominoes[j] or dominoes[i] == dominoes[j][::-1]:
                    ans += 1

        return ans
    


# Let me try to do in O(n)

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        hashMap = {}

        for i in range(len(dominoes)):
            cur = ",".join(map(str, dominoes[i]))
            flip = ",".join(map(str, dominoes[i][::-1]))
            if cur in hashMap or flip in hashMap:
                if cur not in hashMap:
                    cur = flip
                hashMap[cur] += 1
                ans += hashMap[cur]
            else:
                hashMap[cur] = 0


        return ans