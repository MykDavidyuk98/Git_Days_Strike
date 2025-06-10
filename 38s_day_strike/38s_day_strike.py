import math
import random

from accessify import private, protected


# arr_num = [5, 2, 9, 1, 5, 6]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N - 1):

#         for k in range(N-1-i):

#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# print(arr_num)
# bubble_sort(arr_num)
# print(arr_num)
        

# arr_num = [4, 8, 1, 3]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N - 1):

#         for k in range(N - 1 - i):
             
#             if array[k] < array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# print(arr_num)
# bubble_sort(arr_num)
# print(arr_num)


# arr_num = [3, 2, 1, 5, 7, 13, 9]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     swap_count = 0
    
#     for i in range(N - 1):

#         for k in range(N - 1 - i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 swap_count += 1
#     return swap_count

# print(arr_num)
# swap_count = bubble_sort(arr_num)
# print(arr_num, f'Кількість обмінів - {swap_count}')


# arr_num = [1, 2, 3, 4, 5]

# def bubble_sort(array: list) -> str:
#     """Повертає рядок який повідомляє:
#      - Чи завершилось сортування завчасно ?
#      - кількість обмінів при сортуванні (count_swap)
#      - кількість проходів по масиву (pass_count)
#     """
#     N = len(array)
#     count_swap = 0
#     pass_count = 0

#     for i in range(N - 1):
#         swapped = False
#         pass_count += 1
        
#         for k in range(N - 1 - i):

#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 count_swap += 1
#                 swapped = True

#         if not swapped:
            
#             return f'Сортування закінчилось завчасно, кількість обмінів - {count_swap}, кількість проходів {pass_count}'
        
#     return f'Сортування закінчилось звичайним чином, кількість обмінів - {count_swap}, кількість проходів {pass_count}'

# print(arr_num)
# res = bubble_sort(arr_num)
# print(arr_num)
# print(res)


# arr_words = ['banana', 'kiwi', 'apple', 'fig']

# def bubble_sort(array: list, key = lambda x: x) -> None:
#     """Сортує елементи масиву за довжиною елемента(str)
#     """
    
#     N = len(array)

#     for i in range(N - 1):
#         for k in range(N - 1 - i):
#             if key(array[k]) > key(array[k+1]):
#                 array[k], array[k+1] = array[k+1], array[k]

# print(arr_words)
# bubble_sort(arr_words, key = lambda word: word[-1])
# print(arr_words)


# arr_numbers = [7, 2, 4, 1, 9]

# def insertion_sort(array: list) -> None:
#     N = len(array)

#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k] < array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# print(arr_numbers)
# insertion_sort(arr_numbers)
# print(arr_numbers)

# arr_words = ['banana', 'kiwi', 'apple', 'fig']

# def insertion_sort(array: list, key = lambda x: x) -> None:
#     N = len(array)

#     for i in range(1, N):
#         k = i

#         while k > 0 and key(array[k]) < key(array[k-1]):
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# print(arr_words)
# insertion_sort(arr_words, key=len)
# print(arr_words)


# arr_numbers = [4, 1, 8, 3, 6]

# def insertion_sort(array: list) -> None:
#     N = len(array)

#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k] > array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# print(arr_numbers)
# insertion_sort(arr_numbers)
# print(arr_numbers)


# arr_numbers = [3, 2, 1, 5, 812, 11]

# def insertion_sort(array: list) -> int:
#     N = len(array)
#     swap_count = 0

#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k] < array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1
#             swap_count += 1
#     return swap_count

# print(arr_numbers)
# res_swap = insertion_sort(arr_numbers)
# print(arr_numbers, f'Кількість переміщень елементів в масиві - {res_swap} ')


# arr_words = ['banana', 'kiwi', 'apple', 'fig', 'grape']

# def count_vowels(word: str) -> int:
#     vowels = 'aeiouAEIOU'
#     return sum(1 for char in word if char in vowels)

# def insertion_sort(array: list, key = lambda x: x) -> None:
#     N = len(array)

#     for i in range(1, N):
#         k = i

#         while k > 0 and key(array[k]) < key(array[k-1]):
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# print(arr_words)
# insertion_sort(arr_words, key=count_vowels)
# print(arr_words)
