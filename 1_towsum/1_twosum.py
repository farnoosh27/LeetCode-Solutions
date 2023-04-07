
def twosum(nums, target):
    # bruce force solution with time complexity of n*n
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return(i,j)

nums = [0,1,2,2,3,0,4,2]
target = 5


print(twosum(nums,target))


