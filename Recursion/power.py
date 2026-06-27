def power(a,n):
    if n == 0:
        return 1
    # if n == 1:
    #     return a
    
    return a * power(a,n-1)

a = int(input())
n = int(input())
ans = power(a,n)

print(ans)