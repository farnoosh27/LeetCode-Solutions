def replaceElements(arr):
    max_rest = -1
    if len(arr) == 0:
        return([])
    for i in range(len(arr)-1):
        if i != len(arr) - 1:
            max_rest = max(arr[i+1:])
            arr[i] = max_rest
            arr[-1] = -1

    return(arr)


arr = [17,18,5,4,6,1]
print(replaceElements(arr))
# The time complexity of your solution is O(n^2) in the worst case.

# The main reason for this is the use of max() function inside the loop. 
# This function has to scan the remaining portion of the array every time to find the maximum element, which takes O(n) time. Since this operation is performed n-1 times in the loop, the overall time complexity becomes O(n^2).
# To improve the time complexity, you can try to eliminate the use of max() function inside the loop.
#  One way to do this is by keeping track of the maximum element seen so far, and updating it as you iterate through the array in reverse order.
