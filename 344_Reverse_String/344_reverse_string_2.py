
def reverseString(s):
    ## using stack data structure
    stack = []
    for c in s: 
        stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1 
    return(s)

s = ["h","e","l","l","o"]
print(reverseString(s))

# Time complexity O(n)
# Space complexity O(n)