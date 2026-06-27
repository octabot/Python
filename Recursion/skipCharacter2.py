# without explicitly defining new string in body
def remove(s, i=0):
    if i == len(s):
        return ""
    
    # If it's not 'a', keep it and move to the next index
    if s[i] != "a":
        return s[i] + remove(s, i + 1)
    
    # If it IS 'a', skip it and move to the next index
    return remove(s, i + 1)

s = "bacadab"
print(remove(s))