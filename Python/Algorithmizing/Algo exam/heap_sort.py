test_vector = [5,4,9,7,8,4,1,3,2]

def heap_sort(arr):
    n = len(arr)

    # building a max heap
    # iterating over the entire array and call the heapify function on each element
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Extracting elements from heap one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # swapping
        heapify(arr, i, 0)

    return arr

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Checking if left child of root exists and is greater than root
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child
    
    # Checking if right child of root exists and is greater than root
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Changing root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

    # Heapify the root
    heapify(arr, n, largest)


print(heap_sort(test_vector))
