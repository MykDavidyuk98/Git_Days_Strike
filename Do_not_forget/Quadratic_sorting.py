import math
import random

from accessify import private, protected

# ✅ Сортування методом вибору(selection_sort):


# arr_num = [9, 2, 5, 1, 8]
# def selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i

#         for k in range(min_index, N):
#             if array[k] < array[min_index]:
#                 min_index = k

#         array[i], array[min_index] = array[min_index], array[i]

# print(arr_num)
# selection_sort(arr_num)
# print(arr_num)


# Використання lambda функції для сортування за останньою буквою
# 🔹 Вхід: ['kiwi', 'banana', 'fig', 'apple']
# 🔸 Відсортуй список за останьою буквою.

# arr_word = ['kiwi', 'banana', 'fig', 'apple']
# def selection_sort(array: list, key = lambda x: x) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i

#         for k in range(i + 1, N):

#             if key(array[k]) < key(array[min_index]):
#                 min_index = k

#         array[i], array[min_index] = array[min_index], array[i]

# print(arr_word)
# selection_sort(arr_word, key= lambda word: word[-1])
# print(arr_word)


#    Завдання 5. Підрахунок обмінів
# 🔹 Вхід: [5, 2, 4, 1, 3]
# 🔸 Реалізуй сортування вибором і поверни кількість обмінів, які були виконані.

# arr_num = [5, 2, 4, 1, 3]

# def selection_sort(array: list) -> None:
#     N = len(array)
#     swap_count = 0

#     for i in range(N):
#         min_index = i 

#         for k in range(i+1, N):
#             if array[k] < array[min_index]:
#                 min_index = k
        

#         """Перевіряємо чи індекс мін.елемента помінявся у верхньому циклі, 
#         вставляємо перестановку в елементів в умову щоб підрахувати кількість обмінів """
        
#         if min_index != i:
#             array[i], array[min_index] = array[min_index], array[i]
#             swap_count += 1
            
#     return swap_count

# print(arr_num)
# res = selection_sort(arr_num)
# print(arr_num, res)
