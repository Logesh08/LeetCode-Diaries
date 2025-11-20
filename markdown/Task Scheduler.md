# [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/description/)

You are given an array of CPU <code>tasks</code>, each labeled with a letter from A to Z, and a number <code>n</code>. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least**  <code>n</code> intervals between two tasks with the same label.

Return the **minimum**  number of CPU intervals required to complete all tasks.

**Example 1:** 

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: 0.875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3^rd interval, neither A nor B can be done, so you idle. By the 4^th interval, you can do A again as 2 intervals have passed.

**Example 2:** 

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: 0.875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

**Example 3:** 

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: 0.875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

**Constraints:** 

- <code>1 <= tasks.length <= 10^4</code>
- <code>tasks[i]</code> is an uppercase English letter.
- <code>0 <= n <= 100</code>

---

## Solution

```python
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
```