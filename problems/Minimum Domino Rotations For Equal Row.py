# LeetCode Problem 1007: Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/


# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

# If it cannot be done, return -1.

 

# Example 1:


# Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
# Example 2:

# Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

# Constraints:

# 2 <= tops.length <= 2 * 10^4
# bottoms.length == tops.length
# 1 <= tops[i], bottoms[i] <= 6





# First time in my life I have solved a dominos problem on my own!!
# It was medium level and I was scared, but luckyly I was able to solve it in the first attempt!!
# But I know its not the best answer, so I'll think of imporoving it later.


# Things I tought about:
# 1. top[i] and bottom[i] can be equal, so we can increment just once.
# 2. We can choose the domino which has the maximum number of occurences in the array.
# 3. Then we can count the number of occurences of that domino in the top and bottom arrays.
# 4. Then we can subtract the maximum of the two counts from the length of the array to get the minimum number of rotations.


# And funny enough, I used 3 for loops in this code.
# Which is 3n since it's not nested.
# SO the time complexity is O(n) and space complexity is O(1)


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        hashMap = {}
        choosenDomino = -1
        mmax = -1

        for i in range(n):
            if tops[i] != bottoms[i]:
                hashMap[tops[i]] = hashMap.get(tops[i],0) + 1
                hashMap[bottoms[i]] = hashMap.get(bottoms[i],0) + 1
            else:
                hashMap[tops[i]] = hashMap.get(tops[i],0) + 1
        print(hashMap)
        for key,value in hashMap.items():
            if value >= n:
                mmax = max(value,mmax)
                choosenDomino = key

        if choosenDomino == -1:
            return choosenDomino

        topCount = bottomCount = 0
        
        for i in range(n):
            if tops[i] == choosenDomino:
                topCount += 1
            if bottoms[i] == choosenDomino:
                bottomCount += 1

        return n - max(topCount,bottomCount)
    