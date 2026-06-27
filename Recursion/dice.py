def ways(tar,way=""):
    if tar == 0:
        print(way.strip())
        return 
    if tar < 0:
        return
    
    for j in range(len(d)):
        if d[j]<=tar:
            ways(tar-d[j],way+ str(d[j])+"")
        

def ways2(tar,way=""):
    if tar == 0:
        res.append(way.strip())
        return 
    if tar < 0:
        return
    
    for j in range(len(d)):
        if d[j]<=tar:
            ways2(tar-d[j],way+ str(d[j])+"")    

d = [1,2,3,4,5,6]
tar = 4
res = []
ways(4)
ways2(4)
print(res)
