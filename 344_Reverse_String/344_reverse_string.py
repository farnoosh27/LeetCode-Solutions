
def reverseString(s):
    ## swapping first and last pointer
    ## please pay attention that the string 
    ## should be written in an array format
    l = 0
    r = len(s)-1
    
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return(s)


s = ["h","e","l","l","o"]
print(reverseString(s))