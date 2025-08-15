# [119. Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii/description/)

Given an integer <code>rowIndex</code>, return the <code>rowIndex^th</code> (**0-indexed** ) row of the **Pascal's triangle** .

In **Pascal's triangle** , each number is the sum of the two numbers directly above it as shown:
<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif" style="height: 240px; width: 260px;">

**Example 1:** 

```
Input: rowIndex = 3
Output: [1,3,3,1]
```

**Example 2:** 

```
Input: rowIndex = 0
Output: [1]
```

**Example 3:** 

```
Input: rowIndex = 1
Output: [1,1]
```

**Constraints:** 

- <code>0 <= rowIndex <= 33</code>

**Follow up:**  Could you optimize your algorithm to use only <code>O(rowIndex)</code> extra space?

---

## Solution

```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]

        for _ in range(rowIndex):
            temp = [0] + ans + [0] 
            ans = [temp[i]+temp[i+1] for i in range(len(temp)-1)]

        return ans
```