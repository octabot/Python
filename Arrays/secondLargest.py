arr = [34,434,56,7,83,3,334,434]
n = len(arr)
largest =  float('-inf')               #-ve infinity
second_largest = float('-inf')

for i in range(n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and  arr[i]!=largest:
       second_largest = arr[i]
    else:
        pass

print("Largest:",largest)
print("Second Largest:",second_largest)