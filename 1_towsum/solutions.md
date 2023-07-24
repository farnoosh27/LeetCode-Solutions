## Two Sum
### easy
### array

## Question
This is the most popular LeetCode problem. 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have **exactly one** solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1: 

Input: nums = [2,7,11,15], target = 9

Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Exmple 2: 

Input: nums = [3,2,4], target = 6

Output: [1,2]

## Solutions


Here is a link to NeetCode: https://www.youtube.com/watch?v=KLlXCFG5TnA

1) The brute force method would be to have two for loops and check if any two integers in the nums add up to the target, and if so, return the indices of them._> overall time complexity is :O(n*n)

2) Using hashmap and enumerate function to reduce the time complexity! in our hashmap we are gonna be mapping the value to the index: The basic idea behind using a hashmap is to store the values of the input list as the keys of the hashmap, and their indices as the values of the hashmap. This allows us to quickly check if the complement of a number exists in the list by checking if the difference between the target and the current number is already a **key** in the hashmap.
