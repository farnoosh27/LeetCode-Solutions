# The set data structure is well-suited for this task because it has constant time complexity for
# adding and removing elements, as well as for checking membership (i.e., whether an element is in the set). 
# By using a set to keep track of the distinct characters in the current window,
# we can perform these operations efficiently and without having to iterate over the window every time.

def longestsubarray(s):
    start, end = 0, 0 
    max_len = 0
    char_set = set()

    while end < len(s):
        if s[end] not in char_set:
            char_set.add(s[end])
            end += 1
            max_len = max(max_len, end - start)
        else:
            char_set.remove(s[start])
            start += 1
    return max_len

s = [ 3, 4, 5, 6, 7, 2]
print(longestsubarray(s))


