#Good for small dataset upto 50 or 100 terms
#TC = O(n^2)
#SC = O(1)
#stable , inplace

arr = [11,64, 34, 25, 12, 22, 11, 90]
# arr = [3,2,6,5]
print(arr)
n = len(arr)

for i in range(1,n):
    temp = arr[i]
    j = i-1
    while j >=0 and temp < arr[j]:
        arr[j+1] = arr[j]
        j -= 1 
    arr[j+1] = temp
        

print(arr)