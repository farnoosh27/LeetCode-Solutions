# Boyer-Moore majority vote algorithm. This algorithm is used to find the majority element in an array, 
# which is an element that appears more than ⌊n/2⌋ times (where n is the length of the array).

def majorityElement( nums):
    count = 0
    res = None  # initialize to None
    for n in nums: 
        if count == 0:
            res = n 
        if n == res:
            count += 1
        else:
            count -= 1
    return res


     

nums = [2,1,4,4,4,4,1,4]

print(majorityElement(nums))

# This solution is going to run in O(n) space
