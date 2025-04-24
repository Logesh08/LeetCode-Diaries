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


// Gonna pracrtice the problem with expand around center 



char* longestPalindrome(char* s) {
    int len = strlen(s);
    int maxLen = 0;
    int start = 0;
    int end = 0;

    for(int i=0; i<len; i++) {
        expandFromCenter(s, i, i, &maxLen, &start, &end);
        expandFromCenter(s, i, i+1, &maxLen, &start, &end);
    }

    return strndup(s + start, maxLen);
}

void expandFromCenter(char* s, int left, int right, int* maxLen, int* start, int* end) {
    while(left >= 0 && right < strlen(s) && s[left] == s[right]) {
        if(right - left + 1 > *maxLen) {
            *maxLen = right - left + 1;
            *start = left;
            *end = right;
        }
        left--;
        right++;
    }
}