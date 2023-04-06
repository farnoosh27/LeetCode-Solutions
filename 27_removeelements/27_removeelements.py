
def removeElement( nums, val):
    # I think it would be a good idea to use two pointers and instead of dublicates remove the values that are equal to val.
    # I also, think that k would be the location of l pointer

    l = 0
    for r in range(0, len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
    return(l)

nums = [0,1,2,2,3,0,4,2]
val = 2


print(removeElement(nums, val))


