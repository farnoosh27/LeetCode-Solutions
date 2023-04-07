

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


