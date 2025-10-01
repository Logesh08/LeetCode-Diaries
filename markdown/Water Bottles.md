# [1518. Water Bottles](https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2025-10-01)

There are <code>numBottles</code> water bottles that are initially full of water. You can exchange <code>numExchange</code> empty water bottles from the market with one full water bottle.

The operation of drinking a full water bottle turns it into an empty bottle.

Given the two integers <code>numBottles</code> and <code>numExchange</code>, return the **maximum**  number of water bottles you can drink.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/sample_1_1875.png" style="width: 500px; height: 245px;">

```
Input: numBottles = 9, numExchange = 3
Output: 13
Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
Number of water bottles you can drink: 9 + 3 + 1 = 13.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/01/sample_2_1875.png" style="width: 500px; height: 183px;">

```
Input: numBottles = 15, numExchange = 4
Output: 19
Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
Number of water bottles you can drink: 15 + 3 + 1 = 19.
```

**Constraints:** 

- <code>1 <= numBottles <= 100</code>
- <code>2 <= numExchange <= 100</code>


---

## Solution

```python
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles > 0:
            numBottles %= numExchange
            ans += numBottles
        return ans
```