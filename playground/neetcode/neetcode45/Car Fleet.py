from typing import List

# 5min 23 secs
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []

        for pair in pairs:
            p, s = pair
            time = (target - p) / s  # time = distance / speed
            if stack and stack[-1] >= time:
                pass
            else:
                stack.append(time)

        return len(stack)