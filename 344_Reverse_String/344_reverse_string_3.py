
def reverseString(s):
    ## recursive solution 
    def reverse(l,r):
        if l < r: 
            s[l], s[r] = s[r], s[l]
            reverse(l+1, r-1)
    reverse(0, len(s)-1)
    return (s)
s = ["h","e","l","l","o"]
print(reverseString(s))

# Time complexity O(n)
# Space complexity O(n)