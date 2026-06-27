# bacadab -> remove a
def remove(s,i=0):
    ns=""
    if i == len(s):
        return ns
    
    if  s[i] != "a":
        ns = ns + s[i]
    
    return ns + remove(s,i+1)
    
s = "bacadab"
print(remove(s))