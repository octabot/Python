# diagonal also allowed
def count(p,r,c):
    if r==1 and c == 1:
        print(p, end=" ")
        return
    
    if r>1 and c>1:
        count(p+"D",r-1,c-1)
    if r>1:
        count(p+"V",r-1,c)
    if c>1:
        count(p+"H",r,c-1)

print("\n")
count("",3,3)
print("\n")