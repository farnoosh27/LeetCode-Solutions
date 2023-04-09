
def topkfrequentelements(nums, k):
    # this is the bucket sort solution
    # but for this bucket sort we are going through the array 
    # the time complexity of a bucket sort is O(n)
  count = {}
    for i in range(len(nums)):
        if nums[i] in count:
            count[nums[i]] += 1
        else:
            count[nums[i]] = 1

    # create a list of lists to store numbers with the same frequency
    freq = [[] for _ in range(len(nums) + 1)]
    for num, count in count.items():
        freq[count].append(num)

    # iterate through the frequency list from the end and add the elements to the result list
    res = []
    for i in range(len(freq) - 1, 0, -1):
        res.extend(freq[i])
        if len(res) == k:
            return res
nums = [0,0,1,1,1,3,3,3,3,2,2,3,3,4]
k = 2
print(topkfrequentelements(nums, k))


        
    
