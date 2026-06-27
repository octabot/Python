def comb(digits, mapp, result, temp = "",index = 0):
    if index == len(digits):
        result.append(temp)
        return
        
    ch = int(digits[index])
    val = mapp[ch]

    for i in range(len(val)):
       # temp += val[i]
        comb(digits, mapp, result, temp + val[i], index+1)
        



mapp = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
digits = "23"
res = []
comb(digits, mapp , res)
print(res)