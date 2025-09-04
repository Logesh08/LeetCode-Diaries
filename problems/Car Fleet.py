from typing import List

# Stack based approach
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(position)):
            time = (target-position[i]) / speed[i]
            stack.append([position[i],time])

        stack.sort(key= lambda x: x[0])

        ans = 1
        cur = stack.pop()

        while stack:
            top = stack.pop()
            if top[1] > cur[1]:
                ans += 1
                cur = top
            else:
                continue

        return ans
    


# No stack approach
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pos_to_speed = {pos : spd for pos, spd in zip(position, speed)}
        max_time = 0
        res = 0
        position = sorted(position)

        for i in range(len(position) - 1, -1, -1):
            pos = position[i]
            time = (target - pos) / pos_to_speed[pos]

            if max_time >= time:
                continue
            max_time = time
            res += 1

        return res 
    

print(Solution().carFleet(12,
[10,8,0,5,3],
[2,4,1,1,3]))