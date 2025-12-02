# [3623. Count Number of Trapezoids I](https://leetcode.com/problems/count-number-of-trapezoids-i/description/?envType=daily-question&envId=2025-12-02)

<p data-end="189" data-start="146">You are given a 2D integer array <code>points</code>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinates of the <code>i^th</code> point on the Cartesian plane.

<p data-end="579" data-start="405">A **horizontal**  **trapezoid**  is a convex quadrilateral with <strong data-end="496" data-start="475">at least one pair**  of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

<p data-end="579" data-start="405">Return the <em data-end="330" data-start="297"> number of unique **horizontal trapezoids**  that can be formed by choosing any four distinct points from <code>points</code>.

Since the answer may be very large, return it **modulo**  <code>10^9 + 7</code>.

**Example 1:** 

<div class="example-block">
Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:

<img alt="" src="https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-6.png" style="width: 250px; height: 250px;"> <img alt="" src="https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-7.png" style="width: 250px; height: 250px;"> <img alt="" src="https://assets.leetcode.com/uploads/2025/05/01/desmos-graph-8.png" style="width: 250px; height: 250px;">

There are three distinct ways to pick four points that form a horizontal trapezoid:

<li data-end="247" data-start="193">Using points <code data-end="213" data-start="206">[1,0]</code>, <code data-end="222" data-start="215">[2,0]</code>, <code data-end="231" data-start="224">[3,2]</code>, and <code data-end="244" data-start="237">[2,2]</code>.
<li data-end="305" data-start="251">Using points <code data-end="271" data-start="264">[2,0]</code>, <code data-end="280" data-start="273">[3,0]</code>, <code data-end="289" data-start="282">[3,2]</code>, and <code data-end="302" data-start="295">[2,2]</code>.
<li data-end="361" data-start="309">Using points <code data-end="329" data-start="322">[1,0]</code>, <code data-end="338" data-start="331">[3,0]</code>, <code data-end="347" data-start="340">[3,2]</code>, and <code data-end="360" data-start="353">[2,2]</code>.

**Example 2:** 

<div class="example-block">
Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:

<img alt="" src="https://assets.leetcode.com/uploads/2025/04/29/desmos-graph-5.png" style="width: 250px; height: 250px;">

There is only one horizontal trapezoid that can be formed.

**Constraints:** 

- <code>4 <= points.length <= 10^5</code>
- <code>–10^8 <= x<sub>i</sub>, y<sub>i</sub> <= 10^8</code>
- All points are pairwise distinct.

---

## Solution

```python

```