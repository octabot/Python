nums = [1,2,3,4,5,8,9,11,7,12,14,13,15,10]
n = len(nums) + 1
s = n*(n+1)//2 
ans = s - sum(nums)
print(ans)