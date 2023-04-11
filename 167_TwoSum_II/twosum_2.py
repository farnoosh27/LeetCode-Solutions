
def twoSum(numbers, target): 
    l = 0
    r = len(numbers) - 1 
    target = 9
    ## brute force --> n*n --> O(n*n)
    ## we can take advantage of the ascending order 
    while l < r:
        curSum = numbers[l] + numbers[r]

        if curSum > target: 
                r -= 1
        elif curSum < target:
            l += 1 
        else: 
            return [l+1, r+1]

nums = [1,3,4,5,7,11]
target = 9

print(twoSum(nums, target))

