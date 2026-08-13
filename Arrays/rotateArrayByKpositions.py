nums = [76,34,56,68,56,56,34,23,25]
print(nums)
n = len(nums)
k = 2
k = k % n
nums = nums[::-1]    #step 1 : reverse array
nums[:k] = nums[:k][::-1]   #step 2: slice the array and reverse , nums[::-1] only will reverse the complete array each time
nums[k:] = nums[k:][::-1]   #step 3: same as step 2

print(nums)