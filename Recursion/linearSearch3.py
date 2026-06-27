# return list -> all indices of found element
def find(n, l, u = [], i=0):
    
    if i == len(l):
        return u
    if n == l[i]: 
        u.append(i) 

    return find(n, l, u ,  i+1)  

l = [1,23,45,23,44,45]
n = int(input())
print(find(n,l))