n = 1
if n<=1:
    flag = False
else:
    flag = True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            flag = False
            break
print(flag)