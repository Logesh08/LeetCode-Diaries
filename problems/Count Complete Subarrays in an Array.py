# LeetCode Problem 2799: Count Complete Subarrays in an Array
# https://leetcode.com/problems/count-complete-subarrays-in-an-array/



# You are given an array nums consisting of positive integers.

# We call a subarray of an array complete if the following condition is satisfied:

# The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
# Return the number of complete subarrays.

# A subarray is a contiguous non-empty part of an array.

 


# Example 1:
# Input: nums = [1,3,1,2,2]
# Output: 4
# Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].

# Example 2:
# Input: nums = [5,5,5,5]
# Output: 10
# Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 


# Constraints:
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 2000





# I attempted to solve this program with my sheer brute force 

# LOL but I got `TLE`

# It took a while to understand this problem it's prety strait forward though

# Guess I'm still an ammateur to code in O(n^3) time complexity
# Let's try to optimize this code



class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        targetUnique = len(set(nums))

        for i in range(n):
            for j in range(i,n):
                if len(set(nums[i:j+1])) == targetUnique:
                    ans += 1

        return ans




# Lets try that if it will be possible to not use the set 
# and use hashMap in the loop and remove values from it

# The thing is in the inner loop every time we are going to add a new item
# So instead of just finding set of whole subset, we can process by just adding one
# item

# Boom, my solution got accepted but still its not a great one!

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        targetUnique = len(set(nums))

        for i in range(n):
            hashMap = {}
            for j in range(i,n):
                hashMap[nums[j]] = hashMap.get(nums[j],0) + 1
                if len(hashMap) == targetUnique:
                    ans += 1
        
        return ans


# The above solution passsed at the worse margin because of the constrains
# In the constrains it's given as 1000 => 10^3
# O(n^2) => 10^6 is lesser than 10^8 so it passed
# O(n^3) => 10^9 is greater than 10^8 so it failed


# I just realised I could do the same with set, without hashMap


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        targetUnique = len(set(nums))

        for i in range(n):
            hashSet = set()
            for j in range(i,n):
                hashSet.add(nums[j])
                if len(hashSet) == targetUnique:
                    ans += 1
        
        return ans






# Now lets try in an another approach by refering other solutions, my tiny 
# brain is at its limit (insert anime sweat emoji here lol)

# Wow this is my new crazy approach 
# Which beats 99.83% of the submissions (2ms)


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        targetUnique = len(set(nums))
        left = 0
        hashMap = {}

        for right in range(n):
            hashMap[nums[right]] = hashMap.get(nums[right],0) + 1
            while len(hashMap) == targetUnique:
                ans += n - right
                hashMap[nums[left]] -= 1
                if hashMap[nums[left]] == 0:
                    del hashMap[nums[left]]
                left += 1

        return ans
    


# It's crazy to think that came from TLE to 900ms and finally to 2 ms


# Wow feeling great!
# I guess it's better if I stick with solving Easy and Medium problems
# They feel sooo goood!!, ee kimochi desu ne!