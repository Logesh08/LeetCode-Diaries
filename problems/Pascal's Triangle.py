# LeetCode Problem 118: Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/


# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30




from typing import List


# This is my first hard worked solution litrally took me an half an hour, omg!!


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        finalAns = [[1]]
        if numRows == 1:
            return finalAns
        prev = [1,1]
        finalAns.append(prev)
        if numRows == 2:
            return finalAns

        for i in range(numRows-2):
            n = (len(prev) // 2)
            newOne = [1]
            for j in range(n):
                newOne.append(prev[j]+prev[j+1])
            prev = newOne + newOne[::-1][1-(len(prev)%2):]
            finalAns.append(prev)

        return finalAns
    



# Demn I found a smartass zesty solution while browsing

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for _ in range(numRows-1):
            temp = [0] + res[-1] + [0]
            row = []

            for i in range(len(res[-1])+1):
                row.append(temp[i]+temp[i+1])
            res.append(row)

        return res