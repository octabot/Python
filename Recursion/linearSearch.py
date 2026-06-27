#present or not
def find(n, l, i=0):
    if i == len(l):
        return False
    return n == l[i] or find(n,l,i+1)
    

l = [1,23,45,12,56,23,44]
n = int(input())
print(find(n,l))
