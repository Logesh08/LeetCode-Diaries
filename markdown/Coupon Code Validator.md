# [3606. Coupon Code Validator](https://leetcode.com/problems/coupon-code-validator/description/?envType=daily-question&envId=2025-12-13)

You are given three arrays of length <code>n</code> that describe the properties of <code>n</code> coupons: <code>code</code>, <code>businessLine</code>, and <code>isActive</code>. The <code>i^th </code>coupon has:

- <code>code[i]</code>: a **string**  representing the coupon identifier.
- <code>businessLine[i]</code>: a **string**  denoting the business category of the coupon.
- <code>isActive[i]</code>: a **boolean**  indicating whether the coupon is currently active.

A coupon is considered **valid**  if all of the following conditions hold:

- <code>code[i]</code> is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (<code>_</code>).
- <code>businessLine[i]</code> is one of the following four categories: <code>"electronics"</code>, <code>"grocery"</code>, <code>"pharmacy"</code>, <code>"restaurant"</code>.
- <code>isActive[i]</code> is **true** .

Return an array of the **codes**  of all valid coupons, **sorted**  first by their **businessLine**  in the order: <code>"electronics"</code>, <code>"grocery"</code>, <code>"pharmacy", "restaurant"</code>, and then by **code**  in lexicographical (ascending) order within each category.

**Example 1:** 

<div class="example-block">
Input: code = ["SAVE20","","PHARMA5","SAVE@20"], businessLine = ["restaurant","grocery","pharmacy","restaurant"], isActive = [true,true,true,true]

Output: ["PHARMA5","SAVE20"]

Explanation:

- First coupon is valid.
- Second coupon has empty code (invalid).
- Third coupon is valid.
- Fourth coupon has special character <code>@</code> (invalid).

**Example 2:** 

<div class="example-block">
Input: code = ["GROCERY15","ELECTRONICS_50","DISCOUNT10"], businessLine = ["grocery","electronics","invalid"], isActive = [false,true,true]

Output: ["ELECTRONICS_50"]

Explanation:

- First coupon is inactive (invalid).
- Second coupon is valid.
- Third coupon has invalid business line (invalid).

**Constraints:** 

- <code>n == code.length == businessLine.length == isActive.length</code>
- <code>1 <= n <= 100</code>
- <code>0 <= code[i].length, businessLine[i].length <= 100</code>
- <code>code[i]</code> and <code>businessLine[i]</code> consist of printable ASCII characters.
- <code>isActive[i]</code> is either <code>true</code> or <code>false</code>.