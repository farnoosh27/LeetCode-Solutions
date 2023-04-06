#The majorityElement function takes an input parameter nums 
# which is a list of integers, and it returns the majority element as an integer.
# first, we will creat a hashmap
# then check for where the frequency is more than n/2

def majorityElement(nums):
    ## making the hashmap
    count = {}
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1
        
        if count[nums[i]] > n/2:
            return(nums[i])
        

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))

