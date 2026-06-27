# Return the list without passing the argument
def find(n, l, i=0):
    u  = []
    if i == len(l):
        return u
    if n == l[i]: 
        u.append(i) 

    return u + find(n, l, i+1)  

l = [1,23,45,23,44,44,45]
n = int(input())
print(find(n,l))