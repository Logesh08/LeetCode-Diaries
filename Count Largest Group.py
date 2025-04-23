# LeetCode Problem 1399: Count Largest Group
# https://leetcode.com/problems/count-largest-group/

# You are given an integer n.

# Each number from 1 to n is grouped according to the sum of its digits.

# Return the number of groups that have the largest size.

 


# Example 1:
# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.

# Example 2:
# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
 


# Constraints:
# 1 <= n <= 10^4





class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = {}
        largestGroup = 0
        ans = 0
        for i in range(1,n+1):
            cur_sum = 0
            for c in str(i):
                cur_sum += int(c)
            hashMap[cur_sum] = hashMap.get(cur_sum,0) + 1
            if hashMap[cur_sum] > largestGroup:
                largestGroup = hashMap[cur_sum]
                ans = 1
            elif hashMap[cur_sum] == largestGroup:
                ans += 1

        return ans



# I just modfied using just int to caclulate sum it imporoved the performance drastically
# Beats 75% of the submissions


class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = {}
        largestGroup = 0
        ans = 0
        for i in range(1,n+1):
            cur_sum = 0
            temp = i
            while temp > 0:
                cur_sum += temp %10
                temp //= 10
            hashMap[cur_sum] = hashMap.get(cur_sum,0) + 1
            if hashMap[cur_sum] > largestGroup:
                largestGroup = hashMap[cur_sum]
                ans = 1
            elif hashMap[cur_sum] == largestGroup:
                ans += 1

        return ans
    

# Now we can move the if statements outside the loop and
# check if the efficenecy changes

# Wow this beats 81.75% of the submissions
# So sometimes its better to avoid if else in each loop!

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hashMap = {}
        for i in range(1,n+1):
            cur_sum = 0
            temp = i
            while temp > 0:
                cur_sum += temp %10
                temp //= 10
            hashMap[cur_sum] = hashMap.get(cur_sum,0) + 1

        largestGroup = 0
        ans = 0
        for key in hashMap:
            if hashMap[key] > largestGroup:
                largestGroup = hashMap[key]
                ans = 1
            elif hashMap[key] == largestGroup:
                ans += 1

        return ans