test_vector = [5,4,9,7,8,4,1,3,2]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    less_then_pivot = [x for x in arr[1:] if x <= pivot]
    greater_then_pivot = [x for x in arr[1:] if x > pivot]

    return quick_sort(less_then_pivot) + [pivot] + quick_sort(greater_then_pivot)

print(quick_sort(test_vector))