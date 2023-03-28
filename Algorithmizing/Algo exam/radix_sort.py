test_vector = [170, 45, 75, 90, 802, 24, 2, 66]

def radix_sort(arr):

    # defines max number of digits
    max_digit = len(str(max(arr)))

    # variable "digit" takes on values from 0 to "max_digit" - 1.
    for digit in range(max_digit):

        # creating 10 buckets (0-9); "_" means empty variable and states that the variable will not be used later in the code.
        buckets = [[] for _ in range(10)]

        for num in arr:
            # calculates the value of the current digit being considered by the for loop
            digit_num = (num // (10**digit)) % 10
            buckets[digit_num].append(num)
            
        # arr = []
        # for bucket in buckets:
        #     for num in bucket:
        #         arr.append(num)
        arr = [num for bucket in buckets for num in bucket]

    return arr

print(radix_sort(test_vector))