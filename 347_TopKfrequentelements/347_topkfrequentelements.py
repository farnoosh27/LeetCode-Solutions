
def topkfrequentelements(nums, k):
    # this is the bucket sort solution
    # but for this bucket sort we are going through the array 
    # the time complexity of a bucket sort is O(n)
    count = {}
    freq = [[] for i in range(len(nums)+1)]
    for n in nums: 
        count[n] = 1 + count.get(n,0)

    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
nums = [0,0,1,1,1,3,3,3,3,2,2,3,3,4]
k = 2
print(topkfrequentelements(nums, k))


        
    