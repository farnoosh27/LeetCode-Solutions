## Valid Palindrome
### easy
### string
## Question

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise:

example 1:

Input: s = "anagram", t = "nagaram"

Output: true

example 2: 

Input: s = "rat", t = "car"

Output: false

## Solution

Here is the NeetCode solution: https://www.youtube.com/watch?v=9UtInBqnCgA

Overall, the time complexity of the validpalindrome function is O(n^2), where n is the length of the input string. This is because the loop in the function iterates n times, and for each iteration, there is a potentially O(n)-time operation (string replacement) followed by an O(n)-time operation (string reversal). In the worst-case scenario, where every character in the input string needs to be replaced, the time complexity of the function would be O(n^3).
