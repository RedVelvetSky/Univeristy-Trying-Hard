test_vector = [5,4,9,7,8,4,1,3,2]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # dividing the array in two halves
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # recursively sort each other
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # merge the sorted halves back together
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort(test_vector))