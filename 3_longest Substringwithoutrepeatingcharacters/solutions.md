## Longest Substring Without Repeating Characters
### string 
### medium 
### sliding window

## Question
Given a string s, find the length of the longest substring without repeating characters.

Example 1: 

Input: s = "abcabcbb"

Output: 3

Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"

Output: 1

Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"

Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


## Solution: 

The NeetCode solution for that can be found at: https://www.youtube.com/watch?v=wiGpQwVHdE0

This question is the best answered with **sliding window** technique. 

"The sliding window technique involves maintaining a window that contains only distinct characters. We start with a window of size 0 (i.e., an empty set), and add characters to the window one by one as we slide the window to the right. Whenever we encounter a repeating character, we remove the leftmost character(s) from the window until we have a window of distinct characters again."
## Time and Space Complexity
Time complexity: The time complexity of this algorithm is O(n), where n is the length of the input array 's'. This is because the while loop runs once for each element in the array, and each operation inside the loop (adding, removing, and checking membership in the set) has constant time complexity.

Space complexity: The space complexity of the algorithm is O(k), where k is the size of the character set (i.e., the number of distinct characters) in the input array. This is because the size of the set used to track the distinct characters in the current window is at most k. In the worst case, where all characters in the input array are distinct, the space complexity would be O(n). However, in practice, the size of the character set is often much smaller than n, so the space complexity is usually much less than O(n).
