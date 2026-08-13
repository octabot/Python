nums = [-2,1,3,2,4]
n = len(nums)
#brute force    -> O(n2)

maxi = float('-inf')
for i in range(n):
    total = 0
    for j in range(i,n):
        total += nums[j]
        maxi = max(total, maxi)
print("Brute force max",maxi)

#kadane's algo
maxi2 = float('-inf')
total2 = 0
for i in range(n):
    total2 += nums[i]              #step 1
    maxi2 = max(maxi2,total2)      #step 2
    if total2 < 0:                 #step 3
        total2 = 0
print("Kadane's max",maxi2)