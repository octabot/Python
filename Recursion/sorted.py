def sorted(arr, i = 0) -> bool:

    if i == len(arr)-1:
        return True
    
    if arr[i] > arr[i+1]:
        return False

    return sorted(arr, i+1)

arr = [21,36,5896,77777]
print(sorted(arr))