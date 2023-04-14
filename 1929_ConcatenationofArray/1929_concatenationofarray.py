def getConcatenation(nums):
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans
nums = [1,1,1,3,3,4,3,2,4,2]
print(getConcatenation(nums))