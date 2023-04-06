
## 26 remove duplicates
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:



## solution:
There will be two pointers left and right:
for this question we can not use hashmap because we need to do the operation inplace
 we need to us two pointers:
            # l for left --> tell us the next unique value
            # l also tells us how many unique values
            # r for right --> scanning throught the array

