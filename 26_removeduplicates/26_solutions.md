
## Remove Duplicates 
### easy
### array
### in-place

## Question
Given an integer array nums sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Custom Judge:

The judge will test your solution with the following code:


int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];

## solution:

Neet Code explaination video: https://www.youtube.com/watch?v=DEJAZBq0FDA

There will be two pointers left and right:

for this question we can not use hashmap because we need to do the operation inplace

 we need to us two pointers:
            # l for left --> tell us the next unique value
            # l also tells us how many unique values
            # r for right --> scanning throught the array

## Time Complexity:
Each pointer iterates over the same array, so, the time complexity is O(2.n) which we can assume O(n)
The space complexity of the given function is O(1) or constant space complexity.


