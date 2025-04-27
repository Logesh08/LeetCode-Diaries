// LeetCode Problem 14: Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/


// Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

 

// Example 1:

// Input: strs = ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: strs = ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
 

// Constraints:

// 1 <= strs.length <= 200
// 0 <= strs[i].length <= 200
// strs[i] consists of only lowercase English letters if it is non-empty.









class Solution {
    public String longestCommonPrefix(String[] strs) {
        StringBuilder ans = new StringBuilder();
        int minLen = Integer.MAX_VALUE;
        for (String str : strs) {
            minLen = Math.min(minLen, str.length());
        }

        for (int i = 0; i < minLen; i++) {
            char c = strs[0].charAt(i);
            boolean flag = false;
            for (String str : strs) {
                if (str.charAt(i) != c) {
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
            ans.append(c);
        }

        return ans.toString();
    }
}