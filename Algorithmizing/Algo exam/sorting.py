num = []
test_vector = [5,4,9,7,8,4,1,3,2]

def entering_arr_befor_minus_one(arr):
    flag = ["true"]
    while flag[0] != "false":
        temp = int(input())
        arr.append(temp) if  temp != -1 else flag.insert(0, "false")

print("Entered sequence: ", test_vector)

def selection_sort(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]

def insertion_sort(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(0, len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

# entering_arr_befor_minus_one(num)
bubble_sort(test_vector)
# insertion_sort(num)
# selection_sort(num)

print(test_vector)

# print('\n'.join(num))

# print("Sorted sequence: ", num)