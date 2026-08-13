nums = [1,1,2,3,4,5,5,5,6,7,8,8,8]
print(nums)
n = len(nums)
i,j = 0,1
while j<n:
    if nums[i] != nums[j]:
        nums[i+1], nums[j] = nums[j], nums[i+1]
        i+=1
    j+=1

print(f"nums :{nums}\nUnique Elements :{i+1}")
