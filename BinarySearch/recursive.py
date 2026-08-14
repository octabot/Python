def binarySearch(nums,target,low,high):
    if low>high:                   #Base case
        return -1
    
    mid  = (low + high)//2
    if nums[mid] ==  target:
        return mid
    elif nums[mid] < target:
        low = mid +1
        return binarySearch(nums,target,low,high)
    else:
        high = mid -1
        return binarySearch(nums,target,low,high)


nums = [1,2,23,34,45,56,77,88,89]
target = int(input())
n = len(nums)
ans = binarySearch(nums,target,0,n-1)
print(ans)