def Nto1(n):
    if n == 0:
        return
    print(n)

    Nto1(n-1)

n = int(input())
Nto1(n)