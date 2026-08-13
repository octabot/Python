def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
a,b = 12,18
print(gcd(a,b))