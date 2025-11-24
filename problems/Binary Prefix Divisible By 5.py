from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []

        binString = ''.join(str(c) for c in nums)
        for i in range(len(nums)):
            res.append(int(binString[:i+1], 2) % 5 == 0)

        return res
    

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []

        binString = ''
        for i in range(len(nums)):
            binString += str(nums[i])
            if int(binString, 2) % 5 == 0:
                binString = ''
                res.append(True)
            else:
                res.append(False)


        return res
    

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []

        cur = 0
        for n in nums:
            cur = (cur << 1) + n
            res.append(cur % 5 == 0)

        return res
    


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []

        cur = 0
        for n in nums:
            cur = ((cur << 1) + n) % 5
            res.append(cur % 5 == 0)

        return res
    
    

Solution().prefixesDivBy5([1,0,1])