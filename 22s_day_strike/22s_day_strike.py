import math
import random

count_done_quest = 18
# Сортувати методом вставки лише додатні числа у списку, залишаючи інші числа (нуль і від’ємні) на своїх місцях.


# Сортування масиву методом вставок (insert_sort)
# Є список цілих чисел. Відсортуй його за зростанням методом вставки.
# arr = [5, 2, 9, 1, 5, 6]

# mas = [5, 2, 9, 1, 5, 6]

# def insert_sort (array: list):
#     len_arr = len(array)
#     for i in range(1, len_arr):
#         for k in range(i, 0, -1):
#             if array[k-1] > array[k]:
#                 array[k-1], array[k] = array[k], array[k-1]
#     return []
# insert_sort(mas)
# print(mas)

# def insert_sort(array: list) -> None:
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k] < array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1
# insert_sort(mas)
# print(mas)


# Задача 2: Сортування слів за абеткою
# Дано список слів. Відсортуй його в алфавітному порядку методом вставки.
# words = ["banana", "apple", "cherry", "date"]

# words_mas = ['banana', 'apple', 'cherry', 'date']

# def insert_sort(array: list) -> None:
#     """Function get unsorted array in argument and 
#        return sorted array by insertion method"""
    
#     N = len(array)
#     for i in range(1, N):
#         for k in range(i, 0, -1):
#             if array[k] < array[k-1]:
#                 array[k], array[k-1] = array[k-1], array[k]
#     return array

# insert_sort(words_mas)
# print(words_mas)


# Дано список цілих чисел. Відсортуй його за спаданням (від більшого до меншого) методом вставки.
# → [4, 3, 2, 1]
# arr = [3, 1, 4, 2]

# def reverse_insert_sort (array: list) -> None:
#     N = len(array)
#     for i in range( 1, N):
#         k = i
#         while k > 0 and array[k] > array[k-1]:
#             array[k-1], array[k] = array[k], array[k-1]
#             k -= 1
#     return array

# mas = [3, 1, 4, 2]
# reverse_insert_sort(mas)
# print(mas)


# Дано список слів. Відсортуй їх за довжиною методом вставки (від коротких до довгих).
# words = ["dog", "elephant", "cat", "ant"]

# def insert_sort_len_words (array: list) -> None:
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and len(str(array[k-1])) > len(str(array[k])):
#             array[k-1], array[k] = array[k], array[k-1]
#             k -= 1
#     return array

# words = ['dog', 'elephant', 'cat', 'ant']
# insert_sort_len_words(words)
# print(words)
# count_done_quest = 4


# Є список дійсних (float) чисел.
# Перед сортуванням кожне число потрібно округлити до найближчого цілого, 
# а потім відсортувати отримані значення методом вставки.
# Результатом має бути список округлених і відсортованих значень.
# arr = [3.6, 1.2, 2.8, 4.9]

# def insert_sort (array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         array[i] = round(array[i])

    
#     for i in range(1, N):
#         k = i
#         array[i] = round(array[i])
#         while k > 0 and array[k-1] > array[k]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# mas = [3.6, 1.2, 2.8, 4.9]
# print(insert_sort(mas))


# def bubble_sort_algorithm (array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
    

# mas = [-8, 6, -12, 13, 5, 2]
# print(mas)
# bubble_sort_algorithm(mas)
# print(mas)


# Є список слів (рядків). Відсортуй його за зростанням (алфавітно) за допомогою методу бульбашки.
# words = ['pear', 'apple', 'banana', 'kiwi']

# def bubble_sort_algorithm (array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# mas_words = ['pear', 'apple', 'banana', 'kiwi', 'watermelon', 'orange']
# bubble_sort_algorithm(mas_words)
# print(mas_words)


# Сортування чисел за модулем
# Є список чисел з від’ємними значеннями.
# Відсортуй список за зростанням абсолютного значення (тобто за abs(x)), використовуючи метод бульбашки.
# arr = [-3, -7, 2, 1, -1]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         for k in range(0, N-1-i):
#             if abs(array[k]) > abs(array[k+1]):
#                 array[k], array[k+1] = array[k+1], array[k]

# arr = [-3, -7, 2, 1, -1]
# bubble_sort(arr)
# print(arr)


# Сортування чисел за кількістю цифр
# Є список цілих чисел (як додатних, так і від’ємних). Відсортуй їх за зростанням кількості цифр у числі (не враховуючи знак).
# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         for k in range(0, N-1-i):
#             if len(str(abs(array[k]))) > len(str(abs(array[k+1]))):
#                 array[k], array[k+1] = array[k+1], array[k]

# mas_numbers = [1002, -2, 45, -9999, 7, -394, -40, 57234]
# bubble_sort(mas_numbers)
# print(mas_numbers)


# arr = [3, 8, 1, 6, 5, 4]
# N = len(arr)
# even_indexes = [i for i in range(N) if arr[i] % 2 == 0]
# even_value = [arr[i] for i in (even_indexes)]

# def bubble_sort_algorithm(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         k = i
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort_algorithm(even_value)
# print(even_value)

# for idx, val in zip(even_indexes, even_value):
#     arr[idx] = val
# print(arr)


# mas = [1, -10, 5, 15, 13, 10, -123]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         k = i
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(mas)
# print(mas)

# mas = [-15, -20, 5, 14, 123, 34, 25]

# def insert_sort(array: list) -> None:
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k-1] > array[k]:
#             array[k-1], array[k] = array[k], array[k-1]

# insert_sort(mas)
# print(mas)

# впорядкувати масив методом вставок(вибору) - insert_sort, 
# в порядку спадання від більшого до меньшого
# mas = [34, 12, 10, -5, 20, -17]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         k = i
#         for k in range(0, N-1-i):
#             if array[k] < array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(mas)
# print(mas)

# def insert_sort(array: list) -> None:
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k-1] < array[k]:
#             array[k-1], array[k] = array[k], array[k-1]
#             k -= 1

# insert_sort(mas)
# print(mas)

# mas = [1, 10, -5, 34, 56, 32, 102, 342, 3]
# mas = sorted(mas)
# print(f'Масив має наступний вигляд: {mas}')
# target_num = int(input('Введіть число для пошуку в масиві: '))
# flag = False
# def binary_search(array: list, target: int) -> int:
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1 

# binary_search(mas, target_num)
# print(f'Число {target_num} в масиві має індекс {binary_search(mas, target_num)}')


# mas = [-10, 5, -15, 1, 14, 12, 10 , 112, 320]

# def insert_sort(array: list) -> None:
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k] > array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# insert_sort(mas)
# print(mas)

# mas = ['процесор', "команда", "флешка", "абрикос", "брелок", "клавіатура"]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         k = i
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(mas)
# print(mas)

# mas = [random.randint(1,8) for i in range(10)]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         k = i
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(mas)
# print(mas)

# mas = [random.randint(4,11) for i in range(12)]
# print(mas)


# def insert_sort(array: list) -> None:
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k-1] < array[k]:
#             array[k-1], array[k] = array[k], array[k-1]
#             k -= 1

# insert_sort(mas)
# print(f'Відсортований масив має наступний вигляд:\n{mas}') 

# mas = [random.randint(1, 20) for i in range(11)]
# mas = sorted(mas)
# print(mas)
# target_num = int(input('Введіть шукане число: '))

# def binary_search (array: list, target: int) -> int:
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1

# result_index = binary_search(mas, target_num)
# if result_index == -1:
#     print(f'Числа {target_num} в масиві немає!!!')
# else:
#     print(f'Число {target_num} в масиві має індекс: {result_index}')


# mas_numbers = [random.randint(-5,10) for i in range(10)]
# print(mas_numbers)
# condition_request = input('Введіть фільтр: відємне / додатнє / парні: ')

# def print_filtred (array: list, target: str) -> list:
#     N = len(array)
#     filtred_mas = []
#     if target == 'відємне':
#         for i in array:
#             if i < 0:
#                 filtred_mas.append(i)
#     elif target == 'додатнє':
#         for i in array:
#             if i > 0:
#                 filtred_mas.append(i)
#     elif target == 'парні':
#         for i in array:
#             if i % 2 == 0:
#                 filtred_mas.append(i)
#     else:
#         return -1 
#     return filtred_mas

# found_mas = print_filtred(mas_numbers, condition_request)
# print(found_mas)








