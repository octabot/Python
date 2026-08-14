nums = [1,2,23,34,45,56,77,88,89]
target = int(input())

n = len(nums)
low, high = 0, n-1
ans = -1
while low<=high:
    mid = (low + high)//2
    if nums[mid] == target:
        ans = mid
        break
    elif target > nums[mid]:
        low = mid +1
    else:
        high = mid -1
        
if ans == -1:
    print("Not Found")
else:
    print(f'{target} found at index {ans}')