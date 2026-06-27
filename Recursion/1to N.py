def Nto1(n):
    if n == 0:
        return
    
    #call
    Nto1(n-1)
    #kaam
    print(n)

n = int(input())
Nto1(n)