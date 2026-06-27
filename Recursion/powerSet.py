def pows(l, ans = [],i=0):
    if i==len(l):
        print(ans, end=" ")
        return
    pows(l,ans,i+1)
    return pows(l,ans+[l[i]],i+1)

l = [1,2,3]
pows(l)