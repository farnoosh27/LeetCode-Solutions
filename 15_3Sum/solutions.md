## 3Sum
### array
### medium
## Question

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must **not contain duplicate triplets**.

example 1 : 

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation: 

nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.

nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.

nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.

## Solution
The NeetCode video solution is provided at this link: https://www.youtube.com/watch?v=jzZsG8n2R9A

1) Of course, the first solution would be to apply a brute force approach that would result in O(n*n*n) time complexity.
2) This approach uses the approaches in solutions for two-sum and two-sum II. 
  a) First we will sort the input array, and check if the adjacent values are the same. ( we are not allowed to have duplicates. 
  b) Using two numbers exactly like two-sum-2
  Time complexity would be O(onlogn) + O(n*2)
  Space complexity: could be O(n) or O(1) because sorting does take some memory in some libraries. 
