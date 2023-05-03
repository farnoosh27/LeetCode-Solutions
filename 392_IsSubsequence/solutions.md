## Is Subsequence
### string
### easy
## Question
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"

Output: true

Example 2: 

Input: s = "axc", t = "ahbgdc"

Output: false

## Solution
The NeetCode solution is provided in the link: https://www.youtube.com/watch?v=99RVfqklbCE

The function uses two pointers i and j to iterate through the characters of string s and string t, respectively. At each iteration, the function compares the current characters of both strings. If the characters are equal, the function increments both pointers. If the characters are not equal, the function increments only the pointer for string t.

### Time and space complexity
The time complexity of the given function is O(n), where n is the length of the longer string t.

The while loop will iterate until either the end of string s is reached or the end of string t is reached. In the best case scenario, where string s is an empty string or has only one character, the while loop will execute once, and in the worst case scenario where both strings have the same length and are identical, the while loop will execute n times.

The space complexity of the function is O(1) because the amount of memory used is constant and independent of the size of the input. The function only uses two pointers and a constant number of variables.
