def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

array =[10, 20, 30]
target = 30
result = linear_search(array, target)

if result != -1:
    print(f"element at index{result}")
else:
    print("element not found")



def binary_search(arr, low, high, target):
    if low>high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid]<target:
        return binary_search(arr, mid+1, high, target)
    else:
        return binary_search(arr, low, mid-1, target)
    
arr =[10, 20, 30]
target = 30
result = binary_search(arr, 0, len(arr)-1, target)

if result != -1:
    print(f"element at index{result}")
else:
    print("element not found")



#bubble sort
my_array = [66, 52, 37, 21, 12, 24, 12, 94, 5]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array: ", my_array)



