# [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23)

Given two **version strings** , <code>version1</code> and <code>version2</code>, compare them. A version string consists of **revisions**  separated by dots <code>'.'</code>. The **value of the revision**  is its **integer conversion**  ignoring leading zeros.

To compare version strings, compare their revision values in **left-to-right order** . If one of the version strings has fewer revisions, treat the missing revision values as <code>0</code>.

Return the following:

- If <code>version1 < version2</code>, return -1.
- If <code>version1 > version2</code>, return 1.
- Otherwise, return 0.

**Example 1:** 

<div class="example-block">
Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

**Example 2:** 

<div class="example-block">
Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

**Example 3:** 

<div class="example-block">
Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".

**Constraints:** 

- <code>1 <= version1.length, version2.length <= 500</code>
- <code>version1</code> and <code>version2</code>only contain digits and <code>'.'</code>.
- <code>version1</code> and <code>version2</code>**are valid version numbers** .
- All the given revisions in<code>version1</code> and <code>version2</code>can be stored ina**32-bit integer** .

---

## Solution

```python
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        ind = 0
        while ind < len(version1) and ind < len(version2):
            a = int(version1[ind])
            b = int(version2[ind])
            if a > b:
                return 1
            elif b > a:
                return -1
            ind += 1
        while ind < len(version1):
            if int(version1[ind]) != 0:
                return 1
            ind += 1
            
        while ind < len(version2):
            if int(version2[ind]) != 0:
                return -1
            ind += 1
            
        return 0
```