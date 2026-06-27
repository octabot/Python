# print all ways to reach end of the maze from start
def count(p,r,c):
    if r==1 and c == 1:
        print(p, end=" ")
        return
    
    if r>1:
        count(p+"D",r-1,c)
    if c>1:
        count(p+"R",r,c-1)

count("",3,3)