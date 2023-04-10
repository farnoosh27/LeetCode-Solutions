##  Best Time to Buy and Sell Stock

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

 1) brute force solution
 2) using two pointers as left and right.

## inreresting point: 

I think that categorizing this problem as a sub-problem of Sliding Window, may not be the most accurate choice!
The problem of finding the maximum profit when buying and selling stocks is typically solved using the two pointers technique, not the sliding window technique.

In this problem, you are given an array of stock prices over a period of time, and you are asked to find the maximum profit that can be obtained by buying and selling at the right time. To solve this problem using the two pointers technique, you would use two pointers, i and j, where i represents the day of the first stock purchase, and j represents the day of the second stock sale. You would then move the pointers in opposite directions while keeping track of the minimum stock price seen so far, and the maximum profit that can be obtained by selling the stock on day j.

In contrast, the sliding window technique is more useful when you need to find the maximum or minimum value of a subarray of fixed length. For example, if you are given an array of numbers and you want to find the maximum sum of a subarray with a fixed length, you can use the sliding window technique by maintaining a window of the desired length and sliding it over the array to find the maximum sum of the subarray within the window.

