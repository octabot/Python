s = "Hello World"
n = len(s)
"""
approach 1
d = {a:0, e:0, i:0, o:0, u:0}
sare character iterate karunga
agr character hoga dictionary me toh vowel +=1 warna consonants +=1

set bhi use kar sakte h instead of dict so that initialize na karne pade key value pairs
"""
# dic = {"A":0, "E":0, "I":0, "O":0, "U":0, "a":0, "e":0, "i":0, "o":0, "u":0}

vset = set("aeiouAEIOU")
vowels, consonants = 0,0
for i in range(n):
    if s[i].isalpha():  # Filter out spaces, digits, and punctuation
        if s[i] in vset:
            vowels +=1
        else:
            consonants +=1

print(f'Vowels : {vowels}\nConsonants : {consonants}')