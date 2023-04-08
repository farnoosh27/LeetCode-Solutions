
def validpalindrome(s):
    alpha = ["a","b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","10"]

    s = s.lower()
    s = s.replace(" ", "")
    for i in s:
        if i not in alpha: 
            s = s.replace(i, "")
            if s == s[::-1]:
                return(True)

s = "A man, a plan, a canal: Panama"
print(validpalindrome(s))


        
    