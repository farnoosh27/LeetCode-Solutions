
##  remove elements (in-place)
### easy
### array
## Question

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

This solution removes all occurrences åof the given value "val" from the input integer array "nums" in-place, and returns the number of elements in the modified array that are not equal to "val".

The solution uses two pointers, "l" and "r", which traverse the array from the beginning and the end respectively. The "l" pointer is initialized to 0, and it points to the position where the next element that is not equal to "val" will be copied. The "r" pointer starts from the beginning of the array and moves towards the end.

For each element that "r" points to, the solution checks if it is equal to "val". If it is not, then the element is copied to the position pointed to by "l", and "l" is incremented by 1. This ensures that all elements that are not equal to "val" are moved towards the beginning of the array, and all elements that are equal to "val" are effectively removed.

After the traversal is complete, the solution returns the value of "l", which represents the number of elements in the modified array that are not equal to "val".


## Solution
just like problem 26, this problem can be solved using two pointers.
