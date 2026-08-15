nums = [1,3,5,6]
target = 7

n = len(nums)
low , high = 0, n-1

lb = n
while low<=high:
    mid = (low+high)//2
    if nums[mid]>=target:
        lb = mid
        high = mid-1
    elif nums[mid]<target:
        low = mid+1

print(lb)
