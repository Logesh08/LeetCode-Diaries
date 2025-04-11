// Leetcode Problem 2234: Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/



// You are given two positive integers low and high.

// An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the last n digits of x. Numbers with an odd number of digits are never symmetric.

// Return the number of symmetric integers in the range [low, high].

 


// Example 1:
// Input: low = 1, high = 100
// Output: 9
// Explanation: There are 9 symmetric integers between 1 and 100: 11, 22, 33, 44, 55, 66, 77, 88, and 99.

// Example 2:
// Input: low = 1200, high = 1230
// Output: 4
// Explanation: There are 4 symmetric integers between 1200 and 1230: 1203, 1212, 1221, and 1230.
 


// Constraints:
// 1 <= low <= high <= 10^4



// I solved the problem using brute force I gueess.
// It's o(n) and it worked only because the range is small. [10^4]
// I will think of other ways to solve the problem.





// Gonna solve using enumeration there are only 2 ranges in which the numbers can be symmetric.


// Hey yoo guys, this same solution beats 100% of submissions in C++


class Solution {
public:
    int countSymmetricIntegers(int low, int high) {
        int count = 0;

        for(int i=low; i<=high; i++){
            if(i >= 10 && i < 100){
                int first = i / 10;
                int second = i % 10;
                if(first == second){
                    count++;
                }
            } else if(i >= 1000 && i < 10000){
                int first = i / 1000;
                int second = (i / 100) % 10;
                int third = (i / 10) % 10;
                int fourth = i % 10;
                if(first + second == third + fourth){
                    count++;
                }
            }
        }

        return count;
    }
};