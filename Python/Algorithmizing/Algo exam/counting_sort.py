test_vector = [5,4,9,7,8,4,1,3,2]

def counting_sort(arr):
    # max value in the array
    max_value = max(arr)

    # creating a counting array to store the count of elements
    count_arr = [0] * (max_value + 1)

    # storing the count of each element
    for i in range(len(arr)):
        count_arr[arr[i]] += 1

    # creating the output array
    output = [0] * len(arr)

    # building the output array
    # output = [item for item, count in enumerate(count_arr) for i in range(count)]
    output_index = 0
    for item, count in enumerate(count_arr):
        for i in range(count):
            output[output_index] = item
            output_index += 1
    return output

print(counting_sort(test_vector))