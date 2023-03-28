test_vector = [5,4,9,7,8,4,1,3,2]

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(test_vector))
