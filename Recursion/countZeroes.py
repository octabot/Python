def count(n, c = 0):

    #base case
    if n<=0:
        return c
    
    #work
    r = n%10

    #call
    if r==0:
        return count(n//10,c+1)
    else:
        return count(n//10, c)

n = int(input())
print(count(n)) #Function call