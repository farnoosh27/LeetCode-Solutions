
def containsDuplicate(nums):
    count = {}
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1

        if count[nums[i]] > 1:
            return(True)

    #       a = set(nums)
    #     if len(a) != len(nums):
    #        return(True)
nums = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(nums))