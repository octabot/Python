a = [3,5,7,8]
b = [2,4,6,9]

c = [0] * (len(a) + len(b))
i,j,k =0,0,0

while i<len(a) and j<len(b):
    if  a[i] < b[j]:
        c[k] = a[i]
        i += 1
    else:
        c[k] = b[j]
        j += 1
    k += 1

while i<len(a):
    c[k] = a[i]
    i += 1
    k += 1
    
while j<len(b):
    c[k] = b[j]
    j += 1
    k += 1

print(c)