// LeetCode Problem 5: Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

// Given a string s, return the longest palindromic substring in s.

// Example 1:
// Input: s = "babad"
// Output: "bab"
// Explanation: "aba" is also a valid answer.

// Example 2:
// Input: s = "cbbd"
// Output: "bb"

// Constraints:
// 1 <= s.length <= 1000
// s consist of only digits and English letters.


// Gonna pracrtice the problem with Manacher's algorithm 



class Solution {
    public String longestPalindrome(String s) {
        if (s.length() < 2) {
            return s;
        }

        StringBuilder sb = new StringBuilder();
        sb.append('#');
        for (char c : s.toCharArray()) {
            sb.append(c);
            sb.append('#');
        }
        sb.append('$');

        String str = sb.toString();
        int n = str.length();
        int[] p = new int[n];
        int center = 0, right = 0;

        for (int i = 1; i < n - 1; i++) {
            if (i < right) {
                p[i] = Math.min(right - i, p[2 * center - i]);
            }
            while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 && str.charAt(i + p[i] + 1) == str.charAt(i - p[i] - 1)) {
                p[i]++;
            }
            if (i + p[i] > right) {
                center = i;
                right = i + p[i];
            }
        }

        int maxLen = 0, maxCenter = 0;
        for (int i = 1; i < n - 1; i++) {
            if (p[i] > maxLen) {
                maxLen = p[i];
                maxCenter = i;
            }
        }

        StringBuilder result = new StringBuilder();
        for (int i = maxCenter - maxLen; i <= maxCenter + maxLen; i++) {
            if (str.charAt(i) != '#') {
                result.append(str.charAt(i));
            }
        }

        return result.toString();
    }
}