arr = [23,45,78,99,24,34,45]
n = len(arr)
a = [0] * (n/2)
b = [0] * (n-(n/2))
for i in range(len):
    pass



def merge(arr,a,b):
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