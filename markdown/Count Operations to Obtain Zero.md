# [2169. Count Operations to Obtain Zero](https://leetcode.com/problems/count-operations-to-obtain-zero/description/?envType=daily-question&envId=2025-11-07)

You are given two **non-negative**  integers <code>num1</code> and <code>num2</code>.

In one **operation** , if <code>num1 >= num2</code>, you must subtract <code>num2</code> from <code>num1</code>, otherwise subtract <code>num1</code> from <code>num2</code>.

- For example, if <code>num1 = 5</code> and <code>num2 = 4</code>, subtract <code>num2</code> from <code>num1</code>, thus obtaining <code>num1 = 1</code> and <code>num2 = 4</code>. However, if <code>num1 = 4</code> and <code>num2 = 5</code>, after one operation, <code>num1 = 4</code> and <code>num2 = 1</code>.

Return the **number of operations**  required to make either <code>num1 = 0</code> or <code>num2 = 0</code>.

**Example 1:** 

```
Input: num1 = 2, num2 = 3
Output: 3
Explanation: 
- Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
```

**Example 2:** 

```
Input: num1 = 10, num2 = 10
Output: 1
Explanation: 
- Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
So the total number of operations required is 1.
```

**Constraints:** 

- <code>0 <= num1, num2 <= 10^5</code>

---

## Solution

```python
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0

        while num1 and num2:
            if num1 > num2:
                operations += num1 // num2
                num1 %= num2
            else:
                operations += num2 // num1
                num2 %= num1

        return operations
```