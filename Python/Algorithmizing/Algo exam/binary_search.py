def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        
        if arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

arr = [2, 3, 4, 10, 40, 56, 70]
x = 40

print("Index of searching element in array is", binary_search(arr, 0, len(arr)-1, x))