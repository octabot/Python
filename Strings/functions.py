s = "I am a CS Student"
print(s.endswith("a"))  #False
print(s.endswith("ent")) #True

print(s.startswith("i")) #False
print(s.startswith("I a")) #True

#slicing
print(s[1:6])  # am a
print(s[-4:-1]) #den

#reverse string
print(s[::-1]) #tnedutS SC a ma I

f = "abx"
print(f.capitalize()) #capitalize first letter
print(f)  #original str didn't change

print(f.replace("x","c")) #replace old with new one
print(f)  #original str didn't change

print(f.find("ba"))  #-1 if not found

print(s.count("a"))   #2
