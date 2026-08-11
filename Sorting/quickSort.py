def partition(nums, low, high):
    pivot = nums[low]
    i,j = low,high
    while i<j:
        while nums[i] <= pivot and i<=high-1:
            i+=1
        while nums[j] >= pivot and j>=low+1:
            j-=1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    nums[low], nums[j] = nums[j], nums[low]
    return j
        

def quick_sort(nums,  low, high):
    if low<high:
        pidx = partition(nums,low,high)
        quick_sort(nums,low,pidx-1)
        quick_sort(nums,pidx+1,high)

nums = [7,4,9,11,23,45,67]
quick_sort(nums, 0, len(nums)-1)
print(nums)