import math
import random
import turtle 

# handwritten modules
import matryoshka

print('')
count_done_quest = 9


# def insert_sort (array: list) -> None:
#     N = len(array)
#     for i in range (1, N):
#         k = i
#         while k > 0 and array[k-1] > array[k]:
#             array[k-1], array[k] = array[k], array[k-1]
#             k -= 1

# mas = [random.randint(1, 7) for i in range(10)]
# insert_sort(mas)
# print(mas)


# Задача 2. Сортування рядків за довжиною
# Є список слів. Відсортуй його за зростанням довжини кожного слова методом вставок.
# Вхід: ['apple', 'cat', 'banana', 'dog']  

# def insert_sort(array: list) -> None:
#     N = len(array)
#     for i in range (1, N):
#         k = i 
#         while k > 0 and len(array[k-1]) > len(array[k]):
#             array[k-1], array[k] = array[k], array[k-1]
#             k -= 1

# words = ['apple', 'kiwi', 'XOR', 'banana', 'Balabanov', 'carwasher']
# insert_sort(words)
# print(words)


# Задача 3. Сортування списку словників за значенням ключа
# Дано список словників, у кожному є ключ 'age'. Відсортуй список за зростанням віку методом вставок.
# Вхід: [{'name': 'Anna', 'age': 22}, {'name': 'Bob', 'age': 19}, {'name': 'Mike', 'age': 25}]  

# def insert_sort_peple (array: list) -> None:
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k-1]['age'] > array[k]['age']:
#             array[k-1], array[k] = array[k], array[k-1]
#             k -= 1

# mas_people = [{'name': 'Anna', 'age': 22}, {'name': 'Sviatoslava', 'age': 19}, {'name': 'Mike', 'age': 25}, {'name': 'Olia', 'age': 18}]
# print(mas_people)
# insert_sort_peple(mas_people)
# for _ in mas_people:
#     print(_)


# Дано відсортований список цілих чисел. Знайди, чи є в ньому задане число x, використовуючи
# arr = [1, 3, 5, 7, 9, 11]

# def binary_search(array: list, target: int) -> int:
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             right = mid -1
#         else:
#             left = mid + 1
#     return -1

# arr_num = [1, 5, 7, 3, 11, 9]
# arr_num = sorted(arr_num)
# print(arr_num)
# target_num = int(input('Введіть число для пошуку в масиві: '))

# flag = binary_search(arr_num, target_num)
# print(f'Число {target_num} в масиві має індекс: {flag}' if flag != -1 else f'Числа {target_num} в масиві немає!!!')


# Задача 2. Індекс першого входження елемента
# У відсортованому списку можуть бути однакові числа. Знайди індекс першого входження числа x за допомогою бінарного пошуку.

# def binary_search (array: list, target: int) -> int:
#     left = 0 
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             result = mid
#             right = mid - 1
#         elif array[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return result

# arr = [1, 3, 2, 3, 2, 2, 5, 7]
# arr = sorted(arr)
# print(arr)
# target = int(input('Ведіть число для пошуку індекса першого такого числа в масиві: '))
# target_index = binary_search(arr, target)
# print(f'індекс числа {target}: {target_index}' if target_index != -1 else f'Числа {target} в масиві немає!!!')


# Задача 3. Позиція для вставки елемента
# У відсортованому списку знайди позицію, куди слід вставити число x, щоб масив залишався відсортованим. 
# Якщо x уже є — поверни його індекс.
# arr = [1, 3, 5, 7]
# x = 6

# def find_insert_position (array: list, target: int) -> int:
#     left = 0
#     right = len(array) - 1
    
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     # Позиція для вставки 
#     return left

# arr = [1, 2, 5, 9, 11, 5, 10, 23]
# arr = sorted(arr)
# print(arr)
# target = int(input('Введіть число для пошуку елемента, визначення індексу для його вставки: '))
# target_index = find_insert_position(arr, target)
# print(f'Число {target} можна поставити на позицію {target_index}')


# Дано список цілих чисел. Відсортуй його за зростанням методом бульбашки.
# [5, 2, 9, 1] → [1, 2, 5, 9]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         k = i
#         swapped = False
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 swapped = True
#         if not swapped:
#            break
# arr = [2, 1, 5, 9]
# bubble_sort(arr)
# print(arr)


# Є список рядків (імен, слів тощо). Відсортуй його в алфавітному порядку методом бульбашки.
# ['banana', 'apple', 'kiwi'] → ['apple', 'banana', 'kiwi']

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         swapped = False
#         for k in range(0, N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 swapped = True
#         if not swapped:
#             break           # Масив уже відсортовано

# arr_words = ['kiwi', 'citrus', 'mango', 'apple', 'range', 'bubblegum', 'onion', 'sulfur']
# bubble_sort(arr_words)
# print(arr_words)

# Сортування словників за значенням ключа 'score'
# Дано список словників, кожен має ключ 'name' і 'score'.
# Відсортуй список за 'score' спаданням методом бульбашки.

# def bubble_sort_by_key (array: dict) -> None:
#     N = len(array)
#     for i in range(0, N-1):
#         swapped = False
#         k = i
#         for k in range (0, N-1-i):
#             if array[k]['score'] < array[k+1]['score']:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 swapped = True
#         if not swapped:
#             break

# arr_dict = [
#     {'name': 'Anna', 'score': 90},
#     {'name': 'Olia', 'score': 70},
#     {'name': 'Kolia', 'score': 110},
#     {'name': 'Angulema', 'score': 98} 
# ]
# bubble_sort_by_key(arr_dict)
# print(arr_dict)

matryoshka.matryoshka(4)
print(matryoshka.matryoshka)


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()