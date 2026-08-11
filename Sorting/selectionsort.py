arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

print(arr)

for i in range(n-1):
    min_idx = i
    for j in range(i+1,n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[min_idx], arr[i] =  arr[i], arr[min_idx]
        
print(arr)