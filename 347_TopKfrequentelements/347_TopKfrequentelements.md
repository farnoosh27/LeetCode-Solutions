##  Top K Frequent Elements
### medium
### array

## Question: 

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]



Example 2:

Input: nums = [1], k = 1

Output: [1]


It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Solution

Here is the NeetCode solution explained on YouTube: https://www.youtube.com/watch?v=YPTqKIgVk-k

1)

2) using heap
3) 
4) using bucket sort algorithm: "Bucket sort is a sorting algorithm that divides an array of elements into several "buckets", where each bucket is then sorted using another sorting algorithm, such as insertion sort, quicksort or merge sort. After sorting each bucket, the buckets are merged back together to produce the final sorted array.

![alt text]([347_TopKfrequentelements/bucketsort.png](https://github.com/farnoosh27/LeetCode-Solutions/blob/9d6e6f0a88246375dbd5d580d062c6b7eb034869/347_TopKfrequentelements/bucketsort.png))


Bucket sort is useful when the input data is uniformly distributed over a range. It has a linear time complexity O(n) for average and best cases, where n is the number of elements in the input array, making it one of the fastest sorting algorithms for such inputs.

The basic idea of bucket sort is to divide the input array into a set of buckets based on some criteria, such as the value of the elements, and then sort each bucket individually using another sorting algorithm. The sorted buckets are then merged back together to produce the final sorted array."


