# [155. Min Stack](https://leetcode.com/problems/min-stack/description/)

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the <code>MinStack</code> class:

- <code>MinStack()</code> initializes the stack object.
- <code>void push(int val)</code> pushes the element <code>val</code> onto the stack.
- <code>void pop()</code> removes the element on the top of the stack.
- <code>int top()</code> gets the top element of the stack.
- <code>int getMin()</code> retrieves the minimum element in the stack.

You must implement a solution with <code>O(1)</code> time complexity for each function.

**Example 1:** 

```
Input

["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output

[null,null,null,null,-3,null,0,-2]

Explanation

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

**Constraints:** 

- <code>-2^31 <= val <= 2^31 - 1</code>
- Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on **non-empty**  stacks.
- At most <code>3 * 10^4</code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.

---

## Solution

```python
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        minVal = min(self.getMin(),val) if self.stack else val
        self.stack.append([val,minVal])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```