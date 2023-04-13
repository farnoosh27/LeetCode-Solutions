## Reverse String
### easy 
### string 

## Question
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

## Solution
Here is the NeetCode solution: https://www.youtube.com/watch?v=_d0T_2Lk2qA&t=457s

If the interviewer asks this question, it's likely they're seeking multiple solutions. Here are three potential approaches:

1) The easiest and most optimal solution for this question is swapping.
2) Another approach that could be used is the stacking method.
3) Recursion is also a viable option to consider.

"The time complexity of this solution is O(n), where n is the length of the input string s. This is because the reverse() function is called recursively on a decreasing range of indices until the indices converge at the middle of the string, so each index is visited exactly once. This gives a time complexity of O(n/2), which is simplified to O(n) since we ignore constant factors and lower-order terms.

The space complexity of this solution is O(n), where n is the length of the input string s. This is because the reverse() function is called recursively on smaller and smaller ranges of indices until the base case is reached, and each call to reverse() creates a new set of local variables and parameters on the function call stack. The maximum depth of the call stack is also proportional to the length of the string, so the space complexity is O(n)."
