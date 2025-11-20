from collections import deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        freq = [0] * 26
        
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        for f in freq:
            if f > 0:
                heapq.heappush(maxHeap, -f)

        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1

            if maxHeap:
                taskCount = heapq.heappop(maxHeap)
                taskCount += 1                     # Cus task count of "A" is in -, so we + it by one
                if taskCount != 0:
                    queue.append([taskCount, time + n])
            else:
                # This is optinal else block, here we can fast forward time,
                # So that queue will start pushing right now
                time = queue[0][1]

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time