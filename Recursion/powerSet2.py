def pows(s, ans = "",i=0):
    if i==len(s):
        print(ans, end=" ")
        return
    pows(s, ans+s[i], i+1)
    return pows(s, ans,i+1)
    

s = "abc"
pows(s)