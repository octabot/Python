# count number of ways to reach end to of the maze from start
def count(r,c):
    if r==1 or c ==1:
        return 1
    
    left = count(r-1,c)
    right = count(r,c-1)

    return left + right

print(count(3,3))