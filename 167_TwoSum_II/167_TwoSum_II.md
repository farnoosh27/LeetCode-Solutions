
##  Two Sum II - Input Array Is Sorted
### array
### medium


## Question

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1: 

Input: numbers = [2,7,11,15], target = 9
  
Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
  
  ## Solution
The approach used in this solution is a two-pointer technique. The idea is to start with two pointers, one at the beginning of the array (l) and the other at the end of the array (r), and move them towards each other until the sum of the numbers pointed to by l and r equals the target number.

First, the function initializes the two pointers, l and r, to point to the first and last element of the array, respectively. Then, the function enters a loop where it checks if the sum of the numbers pointed to by l and r is greater than, less than, or equal to the target number.

If the sum is greater than the target number, it means we need to decrease the sum by moving the r pointer to the left (i.e., decrease r by 1), as the array is sorted in ascending order. This is because the elements to the left of r are smaller than the element pointed to by r, so we need to move r to the left to get a smaller sum.

If the sum is less than the target number, it means we need to increase the sum by moving the l pointer to the right (i.e., increase l by 1), as the array is sorted in ascending order. This is because the elements to the right of l are larger than the element pointed to by l, so we need to move l to the right to get a larger sum.

If the sum is equal to the target number, it means we have found the two numbers that add up to the target number, and we can return their indices (l+1 and r+1).

Overall, this approach has a time complexity of O(n), as we only traverse the array once. This is an improvement over the brute-force approach, which has a time complexity of O(n^2).



