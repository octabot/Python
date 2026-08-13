s = " abababa "
n = len(s)

#method 1
i,j = 0, n-1
flag = True
while i<=j:
    if s[i] != s[j]:
        flag = False
        break
    else:
        i+=1
        j-=1

print("Using two pointer",flag)

#method 2
s2 = " Aabababa "
palindrome = (s2 == s2[::-1])

print("Using reverse string",palindrome)
 