# The faster, non-recursive, memory-efficient way
def remove_efficient(s):
    chars = [char for char in s if char != "a"]  # Creates a list
    return "".join(chars)  # Creates only ONE final string

s = "bacadab"
print(remove_efficient(s))