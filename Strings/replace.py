s = "I can be of him (harshit) only and  none"
#method 1
new = s.replace("harshit","Deepak")
print(new)

#method 2
l = s.split()
l.remove("(harshit)")
l.insert(5,"deepak")

print(" ".join(l))
