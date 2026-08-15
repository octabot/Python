nums = [1,2,4,5,6,6,7,8,9,9]
target = 7
n = len(nums)
floor,  ceil = -1, -1
low, high = 0, n-1

while low <= high:
    mid = (low+high)//2
    if nums[mid] == target:
        floor, ceil = nums[mid], nums[mid]
        break
    elif nums[mid] >  target:
        ceil = nums[mid]
        high = mid-1
    else:
        floor = nums[mid]
        low = mid+1

print(f'Floor {floor}, Ceil {ceil}')