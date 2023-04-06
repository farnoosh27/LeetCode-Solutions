
def removeDuplicates(nums):
    # we need to us two pointers:
        # l for left --> tell us the next unique value
        # l also tells us how many unique values
        # r for right --> scanning throught the array
        # l starts from 1 cause the first value is always unique
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return(l)

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))


        
    
