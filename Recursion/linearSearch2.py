# return first index
def find(n, l, i=0):
    if i == len(l):
        return -1
    if n == l[i]: 
        return i
    else:
        return find(n, l , i+1)
    

l = [1,23,45,12,56,23,44]
n = int(input())
print(find(n,l))