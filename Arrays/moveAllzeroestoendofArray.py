nums = [1,0,2,3,0,0,5,5,6,0,8,0,8]
print(nums)
n = len(nums)
i=0
for j in range(n):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i+=1

print(nums)