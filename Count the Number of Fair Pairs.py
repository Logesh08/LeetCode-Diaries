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


# Guys Holy shit I feel so dumb af, I was tricked lol...
# Seeing this 0 <= i < j < n made me think we should not sort
# but for any two distinct indices in the list it will always be true lol

# Imagine this, we sort everthing and indices are lost
# now we choose two numbers '3' and '5'
# the possibleity of thier index would be like either '3' will be greater or '5' will be greater
# In such case if we can which is smaller is going to be i and larger one is going to be j

# So any two non equal indeces would naturally follow this 0 <= i < j < n
# Even simply imaging two non equal numbers, they also follow the same rule.
# SO this question has a fun twist lol


# Okay, I think two pointer approch will be suitable for this

# Still getting TLE

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        left = 0
        right = len(nums) - 1
        nums = sorted(nums)

        while left < right:
            cur = nums[left] + nums[right]
            if cur >= lower and cur <= upper:
                partition = left + 1
                while partition < right and nums[partition] + nums[left] < lower:
                    partition += 1
                ans += right - partition + 1
                left += 1
            else:
                if cur > upper:
                    right -= 1
                else:
                    left += 1

        return ans
    


# The major mistake I made is that using another while loop which is obviously going to be O(n^2)
# Instead we can use upper bound - lower bound which gives us what we want using the same method

# I mean, any range of a to b as f(a,b) can be converted as 0 to b subtracted from 0 to a-1
# Which is just referred as f(0,b) - f(0,a-1) 
# Ah it's always math

# Beats 98% of the submissions

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.getAllPairs(nums, upper) - self.getAllPairs(nums, lower - 1)
    
    def getAllPairs(self, nums: List[int], target: int) -> int:
        ans = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            cur = nums[left] + nums[right]
            if cur <= target:
                ans += right - left
                left += 1
            else:
                right -= 1

        return ans
    


# Now lets try using binary search which is also a way to solve
# Without using bisect

# It's worse, just solves the problem in the margin
# Not recommended for this particular problem!

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n):
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] > upper:
                    right = mid - 1
                else:
                    left = mid + 1
            ans += left - i - 1

            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[i] + nums[mid] >= lower:
                    right = mid - 1
                else:
                    left = mid + 1
            ans -= left - i - 1

        return ans