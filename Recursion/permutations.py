#Leetcode 46
def perm(index):
    if index == len(l):
        print(l)
        return
    
    for i in range(index,len(l)):
        l[index], l[i] = l[i], l[index]

        perm(index+1) #backtrack

        l[index], l[i] = l[i], l[index]


l = [1, 2, 3]
perm(0)
