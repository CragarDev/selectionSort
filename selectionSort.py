import time

print()
# set up to time the code

start_time = time.time()


# ** Selection Sort **


def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


num_list1 = [6, 5, 3, 1, 8, 7, 2, 4] * 1000

# print(selectionSort(num_list1))
selectionSort(num_list1)


#
end_time = time.time()
# time_elapsed = end_time - start_time
# conver to seconds
# time_elapsed = time_elapsed * 1000
print("time start: ", start_time)
print("Time end: ", end_time)
print("Time elapsed: ", round((end_time - start_time), 2), "sec")
#
#
#
print()
