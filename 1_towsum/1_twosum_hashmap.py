

 # using hashmap to store the complement of each target to that and return if they add up to the target
 # we are using added memory though, the hashmap isn't free
def twosum(nums, target):
    hashmap = {}
    for i, _ in enumerate(nums):
        diff = target - nums[i]
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[nums[i]] = i
    return None


nums = [0,1,2,2,3,0,4,2]
target = 5


print(twosum(nums,target))


