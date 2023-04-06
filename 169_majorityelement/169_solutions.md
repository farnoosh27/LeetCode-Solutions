## 169 LeetCode
### easy
### Question:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

example 1: 

Input: nums = [3,2,3]
Output: 3

example 2: 
Input: nums = [2,2,1,1,1,2,2]
Output: 2

### Solutions: 
This is the question 169 on Leetcode and has two parts:


1) Simple hashmap to store the frequency and then check were the frequency is n/2
2) Using "Boyer Mooyer" algorithm to get rid of the hashmap. here is some information about the follow up solution:
The Boyer-Moore algorithm is an efficient algorithm for finding a pattern within a text string. It was developed by Robert S. Boyer and J Strother Moore in 1977, and it is widely used in computer science and software engineering for its simplicity and effectiveness.

The algorithm works by scanning the text string from left to right and comparing it with the pattern from right to left. This allows the algorithm to skip over sections of the text string that cannot possibly match the pattern, which leads to a significant speedup over naive pattern-matching algorithms.

The Boyer-Moore algorithm uses two main techniques to achieve its efficiency: the "bad character rule" and the "good suffix rule". The bad character rule uses information about the position of the last occurrence of each character in the pattern to skip over sections of the text string that cannot possibly match the pattern. The good suffix rule uses information about the longest suffix of the pattern that matches a prefix of the pattern to skip over sections of the pattern that have already been matched.

By combining these two techniques, the Boyer-Moore algorithm is able to achieve an average-case time complexity of O(n+m), where n is the length of the text string and m is the length of the pattern. This makes it one of the most efficient pattern-matching algorithms in practical use today.
