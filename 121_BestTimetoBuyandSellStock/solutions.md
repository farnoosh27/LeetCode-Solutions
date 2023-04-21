##  Best Time to Buy and Sell Stock


### easy
### array 
#### two pointers
## Question
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]

Output: 5

Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:

Input: prices = [7,6,4,3,1]

Output: 0

Explanation: In this case, no transactions are done and the max profit = 0.

## Solution:
The neetcode solution can be found here: https://www.youtube.com/watch?v=1pkOgXD63yU
 1) brute force solution
 2) using two pointers as left and right.
## Time and Space Complexity
The time complexity of this function is O(n), where n is the length of the prices list. This is because the function iterates over the list once using a while loop, and each iteration performs constant time operations. 

The space complexity is O(1), as the function uses a constant amount of memory regardless of the size of the input. Specifically, the function uses only a few variables to keep track of the maximum profit, the left and right pointers, and the current profit, which do not depend on the input size.
## inreresting point: 

I think that categorizing this problem as a sub-problem of Sliding Window, may not be the most accurate choice! Here is the difference between them: 

Sliding window technique involves maintaining a window of fixed size over an array or string, and sliding the window over it to find a particular pattern or substring. The window moves one element at a time and the elements within the window are processed to find the desired result. This technique is useful when you want to find a substring or pattern in a string or array with a given length, or when you want to find the maximum or minimum value of a subarray with a fixed length.

Two pointers technique, on the other hand, involves using two pointers to traverse an array or string in opposite directions or in the same direction. The pointers are moved based on certain conditions until they meet or until the desired result is obtained. This technique is useful when you want to find pairs or subarrays of elements that meet certain conditions, such as finding a pair of elements that sum up to a particular value, or finding the longest palindrome in a string.

The problem of finding the maximum profit when buying and selling stocks is typically solved using the two pointers technique, not the sliding window technique.

In this problem, you are given an array of stock prices over a period of time, and you are asked to find the maximum profit that can be obtained by buying and selling at the right time. To solve this problem using the two pointers technique, you would use two pointers, i and j, where i represents the day of the first stock purchase, and j represents the day of the second stock sale. You would then move the pointers in opposite directions while keeping track of the minimum stock price seen so far, and the maximum profit that can be obtained by selling the stock on day j.

In contrast, the sliding window technique is more useful when you need to find the maximum or minimum value of a subarray of fixed length. For example, if you are given an array of numbers and you want to find the maximum sum of a subarray with a fixed length, you can use the sliding window technique by maintaining a window of the desired length and sliding it over the array to find the maximum sum of the subarray within the window.

