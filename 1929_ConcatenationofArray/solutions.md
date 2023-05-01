## Concatenation of Array
### array
### easy

## Question: 
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Input: nums = [1,2,1]

Output: [1,2,1,1,2,1]

Explanation: The array ans is formed as follows:

- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

## Solution 
Here is the NeetCode video of the LeetCode questions's solution: https://www.youtube.com/watch?v=68isPRHgcFQ

1) The easiest solution would be to add the array to the array before and add it to the end

2) Another more extensive approach would be to create an output array and take each value and append it, but if for example if the problem was asking for three concatenation we would do it another time. 

### Time and Space complexity
  * Since this is like a dynamic array, and we are taking each value and pushing it through the end O(n) would be the time complexity
  
  * we will technically gonna need extra memory, therefore, the space complexity of this code is also O(n)
