# 0 <= i < j < n, and
# lower <= nums[i] + nums[j] <= upper



# Classic approach will get failed because the question is "Medium" tagged
# And the reason for that is the boundary conditions
# -10^9 to +10^9 , and recently I came accross an youtuber who told 
# brute force approaches can be made till only 10^8

# GOT TLE

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                cur = nums[i]+nums[j]
                if lower <= cur and cur <= upper:
                    ans += 1
        return ans


# Lets see if we can use some different method like enumaration or dp
# Maybe we can try two pointer, cuz we need to use two indices

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0