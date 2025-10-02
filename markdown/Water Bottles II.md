# [3100. Water Bottles II](https://leetcode.com/problems/water-bottles-ii/description/?envType=daily-question&envId=2025-10-02)

You are given two integers <code>numBottles</code> and <code>numExchange</code>.

<code>numBottles</code> represents the number of full water bottles that you initially have. In one operation, you can perform one of the following operations:

- Drink any number of full water bottles turning them into empty bottles.
- Exchange <code>numExchange</code> empty bottles with one full water bottle. Then, increase <code>numExchange</code> by one.

Note that you cannot exchange multiple batches of empty bottles for the same value of <code>numExchange</code>. For example, if <code>numBottles == 3</code> and <code>numExchange == 1</code>, you cannot exchange <code>3</code> empty water bottles for <code>3</code> full bottles.

Return the **maximum**  number of water bottles you can drink.

**Example 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/28/exampleone1.png" style="width: 948px; height: 482px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;">

```
Input: numBottles = 13, numExchange = 6
Output: 15
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
```

**Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2024/01/28/example231.png" style="width: 990px; height: 642px; padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem;">

```
Input: numBottles = 10, numExchange = 3
Output: 13
Explanation: The table above shows the number of full water bottles, empty water bottles, the value of numExchange, and the number of bottles drunk.
```

**Constraints:** 

- <code>1 <= numBottles <= 100 </code>
- <code>1 <= numExchange <= 100</code>

