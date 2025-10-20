# [2011. Final Value of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/?envType=daily-question&envId=2025-10-18)

There is a programming language with only **four**  operations and **one**  variable <code>X</code>:

- <code>++X</code> and <code>X++</code> **increments**  the value of the variable <code>X</code> by <code>1</code>.
- <code>--X</code> and <code>X--</code> **decrements**  the value of the variable <code>X</code> by <code>1</code>.

Initially, the value of <code>X</code> is <code>0</code>.

Given an array of strings <code>operations</code> containing a list of operations, return the **final ** value of <code>X</code> after performing all the operations.

**Example 1:** 

```
Input: operations = ["--X","X++","X++"]
Output: 1
Explanation:The operations are performed as follows:
Initially, X = 0.
--X: X is decremented by 1, X =  0 - 1 = -1.
X++: X is incremented by 1, X = -1 + 1 =  0.
X++: X is incremented by 1, X =  0 + 1 =  1.
```

**Example 2:** 

```
Input: operations = ["++X","++X","X++"]
Output: 3
Explanation: The operations are performed as follows:
Initially, X = 0.
++X: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
X++: X is incremented by 1, X = 2 + 1 = 3.
```

**Example 3:** 

```
Input: operations = ["X++","++X","--X","X--"]
Output: 0
Explanation:The operations are performed as follows:
Initially, X = 0.
X++: X is incremented by 1, X = 0 + 1 = 1.
++X: X is incremented by 1, X = 1 + 1 = 2.
--X: X is decremented by 1, X = 2 - 1 = 1.
X--: X is decremented by 1, X = 1 - 1 = 0.
```

**Constraints:** 

- <code>1 <= operations.length <= 100</code>
- <code>operations[i]</code> will be either <code>"++X"</code>, <code>"X++"</code>, <code>"--X"</code>, or <code>"X--"</code>.

## Solution

```python
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for operation in operations:
            if operation[1] == '+':
                x += 1
            else:
                x -= 1
        return x
```