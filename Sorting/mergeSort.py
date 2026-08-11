def merge(left, right):
    result = []
    i,j = 0,0
    n,m = len(left), len(right)
    while i<n and j<m:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i<n:
        while i<n:
            result.append(left[i])
            i += 1
    if j<m:
        while j<m:
            result.append(right[j])
            j += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]         #slicing
    right = arr[mid:]
    left_sarr = merge_sort(left)        #ek jo element ayega vo sorted hi hoga
    right_sarr = merge_sort(right)

    return merge(left_sarr, right_sarr)

arr = [7,4,9,11,23,45,67]
ans = merge_sort(arr)

print(ans)