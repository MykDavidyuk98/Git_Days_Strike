import random
# 1
# Відсортуй список цілих чисел у порядку зростання методом Bubble Sort.
# arr = [5, 3, 8, 1, 2]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for k in range(N - 1):

#         for i in range(N - 1 - k):

#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]

# bubble_sort(arr)
# print(arr)


# 2
# Відсортуй список дійсних чисел методом Selection Sort (choice sort).
# arr = [3.1, 0.5, 2.8, 1.3, 0.9]

# arr = [3.1, 0.5, 2.8, 1.3, 0.9]

# def selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i

#         for k in range(min_index, N):

#             if array[k] < array[min_index]:
#                 min_index = k

#         array[i], array[min_index] = array[min_index], array[i]

# selection_sort(arr)
# print(arr)

# 3
# Відсортуй список від’ємних чисел методом Insertion Sort.
# arr = [-3, -1, -7, -4, -2]

# arr = [-3, -1, -7, -4, -2]

# def insertion_sort(array: list) -> None:
#     N = len(array)

#     for i in range(1, N):
#         k = i

#         while k > 0 and array[k] > array[k-1]:
#             array[i], array[i+1] = array[i+1], array[i]
#             k -= 1

# insertion_sort(arr)
# print(arr)

arr = [[1, 2] for _ in range(3)]
print(arr)