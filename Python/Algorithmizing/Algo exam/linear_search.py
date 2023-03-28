arr = [2, 3, 4, 10, 40, 56, 70]

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # element found, return its index
    return -1  # element not found

print(linear_search(arr, 10))