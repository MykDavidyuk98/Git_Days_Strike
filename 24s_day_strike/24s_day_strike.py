import math
import random

# mas_two_dimansion = [
#     [34, 23, 6, 9],
#     [35, 11, 54, 23],
#     [15, 40, 3, 44]
# ]

# print(*mas_two_dimansion, sep='\n')
# print(mas_two_dimansion[1][1])

# def sum_of_arr_elements (array: list) -> None:
#     n = 3
#     m = 4
#     sum = 0
#     for i in range(n):
#         for k in range(m):
#             sum += array[i][k]
#     print(f'сума всіх елементів масиву: {sum}')
#     return sum, n, m

# sum_mas, n, m = sum_of_arr_elements(mas_two_dimansion)
# print(f'Сума всіх елементів двохвимірного масиву: {sum_mas}, \nСереднє значення всіх елементів масиву: {sum_mas/(n*m)} ')


# arr_words = [['комірка', "файл", "папка"], ['кома', "миша", "байт"]]

# def print_word_from_arr(array: list) -> None:
#     print(array[0][0])
#     print(array[1][1])

# print_word_from_arr(arr_words)


# arr_number = [[3, 8, 10], [16, 2, 7], [22, 8, 5]]

# sum_first_column = 0
# sum_second_column = 0
# sum_third_column = 0
# N = len(arr_number)

# for i in range(N):
#     for k in range(N):
#         if k == 0:
#             sum_first_column += arr_number[i][k]
#         elif k == 1:
#             sum_second_column += arr_number[i][k]
#         else:
#             sum_third_column += arr_number[i][k]

# print(sum_first_column)
# print(sum_second_column)
# print(sum_third_column)


# arr_number = [[40, 14, 22, 17], [80, 19, 37, 51], [7, 20, 35, 55]]

# min_num_first_row = arr_number[0][0]
# min_num_second_row = arr_number[1][0]
# min_num_third_row = arr_number[2][0]

# for i in range(len(arr_number)):
#     for k in range(len(arr_number[i])):
#         if i == 0 and arr_number[i][k] < min_num_first_row:
#             min_num_first_row = arr_number[i][k]
#         elif i == 1 and arr_number[i][k] < min_num_second_row:
#             min_num_second_row = arr_number[i][k]
#         elif i == 2 and arr_number[i][k] < min_num_third_row:
#             min_num_third_row = arr_number[i][k]

# print(min_num_first_row)
# print(min_num_second_row)
# print(min_num_third_row)

# # Alternate_option, shorter and readable option:
# arr_number = [[40, 14, 22, 17], [80, 19, 37, 51], [7, 20, 35, 55]]

# for row in arr_number:
#     min_num = row[0]
#     for num in row:
#         if num < min_num:
#             min_num = num
#     print(min_num)

# first_tuple, second_tuple = zip([1, 2, 3], ['a', 'b'])
# print(first_tuple)
# print(second_tuple)

# arr_names = ['Bogdan', 'Sofia', 'Kolia']
# arr_ages = [22, 18, 27]

# for name, age in zip(arr_names, arr_ages):
#     print(f'{name} має {age} років')

# sort_list_with_name_age = list(zip(arr_names, arr_ages))
# print(sort_list_with_name_age)

# Задача 1: Ім'я + Вік
# Є два списки:
# names = ["Анна", "Богдан", "Олег"]
# ages = [21, 19, 25]
# Анна має 21 рік

# names = ['Anna', 'Bogdan', 'Slava', 'Vika']
# ages = [23, 18, 46, 14]

# for name, age in zip(names, ages):
#     print(f'{name} має {age} рік')


# students = ["Марія", "Іван", "Оксана"]
# grades = [12, 9, 10]
# Створи новий список results, де кожен елемент — це кортеж з іменем та оцінкою, наприклад:

# [("Марія", 12), ("Іван", 9), ("Оксана", 10)]

# studets = ['Maria', 'Ivan', 'Artem', 'Olia']
# grades = [12, 10, 9, 15]

# studets_with_grades = list(zip(studets, grades))
# print(studets_with_grades)


# Знайди суму кожної пари чисел з однаковим індексом:

# a = [1, 2, 3]
# b = [4, 5, 6]

# for i, k in zip(a, b):
#     print(f'{i} + {k} =', i+k)

