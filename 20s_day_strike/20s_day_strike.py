import math
import random 

# print(5)
# A = [x for x in range(5)]
# B = list(range(5))
# C = A + B 
# print(A)
# print(B)
# print(C)
# print(C[max(A)])
# D = list(random.randint(5,10)for i in range(5))
# print(D)

# A = [random.randint(1,10) for i in range(10)]
# print(A)
# A_max = 0
# for i in range (len(A)):
#     if A[i] > A[A_max]:
#         A[A_max], A[i] = A[i], A[A_max]
# print(A[A_max])


# Напиши функцію, яка сортує список чисел методом вставки у порядку зростання.
# insertion_sort([5, 2, 4, 6, 1, 3])
# Повертає: [1, 2, 3, 4, 5, 6]


# A = [12, 15, 14, 10, 1, 6]
# def insertion_sort(array: list):
#     N = len(array)
#     for top in range(1, N):
#         k = top
#         while k  > 0 and array[k] < array[k-1] :
#             array[k], array[k-1] =  array[k-1], array[k] 
#             k -= 1
#     return array
# print(insertion_sort(A))


# Змодифікуй алгоритм так, щоб він сортував масив у порядку спадання.
# insertion_sort_desc([7, 4, 9, 2])
# Повертає: [9, 7, 4, 2]

# A = [7, 4, 9, 2]
# def insertion_reverse_sort (array: list):
#     N = len(array)
#     for i in range (1, N):
#         k = i
#         while k > 0 and array[k] > array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1
# insertion_reverse_sort(A)
# print(A)


# Сортування рядків за довжиною
# Використовуючи метод вставки, відсортуй список рядків за довжиною (від найкоротших до найдовших).
# insertion_sort_by_length(["apple", "kiwi", "banana", "fig"])
# Повертає: ['fig', 'kiwi', 'apple', 'banana']
# A = ["apple", "kiwi", "banana", "fig"]
# N = len(A)
# def insertion_sort_by_length(array: list, insertions = 0):
#     sort_count = 0
#     for i in range(1, len(array)):
#         top = i
#         while top > 0 and len(array[top-1]) > len(array[top]):
#             array[top-1], array[top] = array[top], array[top-1]
#             top -= 1
#             sort_count += 1
#     return array, sort_count
# sorted_A, insertions = insertion_sort_by_length(A)
# print(sorted_A) 
# print(insertions)





