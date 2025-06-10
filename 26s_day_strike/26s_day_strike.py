import math
import random
import turtle as tr
import re


# for i in range (12):
#     tr.shape('turtle')
#     tr.forward(100)
#     tr.stamp()
#     tr.backward(100)
#     tr.right(360/12)

# a = b = c = 7
# print(a, b, c, id(a), id(b), id(c))

# count = 0
# arg = 0 
# Arg = 0
# print(id(count), id(arg), id(Arg))

# words = 'Fuck You'
# print(words[0], words[5])

# a_1 = 'some text'
# print(chr(1065))

# full_text = '+'.join(('some', 'text', 'here'))
# print(full_text)

# print('COMPUter'.lower())

# a = 'computer'.capitalize()
# print(a)

# some_text = 'пошук'
# method_rfind = some_text.rfind('шук')
# print(method_rfind)

# some_text_you_must_know = 'some of some text men'
# count_men = some_text_you_must_know.count('men')
# count_ome = some_text_you_must_know.count('ome')
# print(count_ome)
# print(count_men)

# family = 'mother and father'
# family_without_father = family.replace('father', 'sister')
# print(family,'\n' + family_without_father)
# print(family.replace('mother', 'brother'))
# print(family)

# a = ('кількість', "входжень")
# b = ('підрядка', "у рядок")
# c = a + b 
# c = ' '.join(c)
# print(c)
# pidrydka_find = c.count('підрядка')
# print(pidrydka_find)
# code_of_k = ord('к')
# print(code_of_k)

# some_text = 'рядок є незмінним типом даних'
# print(some_text.capitalize())
# print(ord(some_text[8]))
# print(some_text.count('м'))
# print(some_text.find('типом'))
# print(len(some_text[8:17]))
# print(some_text[8:17])
# print(len('незмінним'))

# row_1 = 'Операційна'
# row_2 = "система"
# print(len(row_1))
# print(len(row_2))
# sum_of_rows = row_1 + ' ' + row_2
# print(sum_of_rows)
# print(len(sum_of_rows))

# row_1 = 'Принтер LM Laser P1006'
# row_1 = row_1.replace('LM Laser', 'HP LaserJet')
# print(row_1)

# some_row = 'Рим - столиця Італії, Париж - столиця Франції'
# print(ord('м'))
# count_capital = some_row.count('столиця')
# print(count_capital)

# new_row = 'microsoft'
# another_row = 'Word'
# new_row = new_row.capitalize()
# new_row += ' ' + another_row
# count_o = new_row.count('o')

# print(new_row)
# print(count_o)
# print(ord(new_row[5]))


# start_row = 'Інструкція для користувача'
# start_row = start_row.replace('користувача', 'вчителя')
# index_of_for = start_row.find('для')
# print(start_row, f'\n{index_of_for}')

# Напиши програму, яка просить у користувача ім’я і вік, а потім виводить фразу типу:
# Привіт, Оля! Тобі 13 років.

# name = str(input('Введіть імя: '))
# age = int(input('Введіть вік: '))

# print('Привіт, {0}! Тобі {1} років.'.format(name, age))


# Задано ширину та висоту прямокутника. Виведи:
# Прямокутник шириною 4 і висотою 5 має площу 20

# width_rectangle = 10
# height_rectangle = 5
# S_rectangle = width_rectangle * height_rectangle

# print('Прямокутник шириною {0} і висотою {1} має площу {2}'.format(width_rectangle, height_rectangle, S_rectangle))
# print(f'Прямокутник шириною {width_rectangle} і висотою {height_rectangle} має площу {S_rectangle}')

# Є ім’я учня і його оцінки з трьох предметів. Виведи:
# Андрій: математика - 10, фізика - 9, інформатика - 11

# name = 'Вася'
# math = 11
# phisic = 8
# cs = 10

# print('{0}: математика - {1}, фізика - {3}, інформатика - {2}'.format(name, math, cs, phisic))
# print(f'{name}: математика - {math}, фізика - {phisic}, інформатика - {cs}')

# zip() method
# Дано два списки — імена учнів та їхні оцінки. Виведи кожного учня з його оцінкою:

# arr_names = ['Kolia', 'Nastia', 'Marina', 'Sofia']
# arr_grades = [11, 12, 9, 6]
# count_bad_grades = 0
# good_students = []

# for name, grade in zip(arr_names, arr_grades):
#     if grade < 10:
#         count_bad_grades += 1
#     elif grade > 10:
#         good_students.append(name)

#     print(f'Учень {name} має оцінку - {grade}' if grade > 10 
#           else f'Учень {name} має оцінку {grade}, потрібно старатися краще!!')
    

# print(f'Кількість поганих оцінок в класі - {count_bad_grades}')
# print(f'список учнів з гарними оцінками: ', *good_students)
# print(f'Середній бал класу становить - {round(sum(arr_grades)/len(arr_grades), 1)}')
   
# Є відсортований список чисел. Знайди, чи є в ньому задане число.
# Вхідні дані
# arr = [1, 3, 5, 7, 9, 12, 17]
# target = 7
# Число 7 знайдено на позиції 3


# arr_numbers = sorted(random.randint(2,15) for i in range(10))
# print(arr_numbers)
# target = int(input('Введіть число для пошуку його індекса в масиві: '))

# def binary_search(array: list, target: int) -> None:
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             return mid
#         elif array[mid] < target:
#             left = mid + 1
#         else: 
#             right = mid - 1
#     return -1

# target_index = binary_search(arr_numbers, target)

# print(f'Число {target} в масиві має індекс: {target_index}'  if target_index != -1
#       else f'Числа {target} в масиві не знайдено! Спробуйте ще раз')


# arr_numbers = sorted(random.sample(range(2, 15),10))
# print(arr_numbers)

# У відсортованому списку є повторювані числа. Знайди індекс першого входження заданого числа.
# arr_numbers = [2, 4, 4, 4, 6, 7, 10]
# print(arr_numbers)
# target = int(input('Введіть число для пошуку в масиві: '))
# result = -1 

# def binary_search(array: list, target: int) -> None:
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             result = mid
#             right = mid - 1
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result

# target_index = binary_search(arr_numbers, target)

# print(f'Перше входження числа {target} в масиві має індекс: {target_index}' if target_index != -1
#       else f'Числа {target} в масиві не знайдено!!')

# Пошук останього індекса елемента в масиві з повторюваними числами

# arr_numbers = sorted(random.randint(2, 18) for i in range(15))
# target = int(input(f'{arr_numbers}\nВведіть число для пошуку останього індекса такого елемента в масиві:'))

# def binary_search(array: list, target: int) -> None:
#     left = 0
#     right = len(array) - 1
#     result = -1

#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             result = mid
#             left = mid + 1
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result

# target_index = binary_search(arr_numbers, target)

# print(f'Число {target} в масиві зустріається в останьому елементі з індексом: {target_index}' if target_index != -1
#       else f'Число {target} в масиві не знайдене! Спробуйте ще раз')


# Пошук першого індекса елемента в масиві з повторюваними числами

# arr_numbers = sorted(random.randint(2,9) for i in range(15))
# print(arr_numbers)
# target = int(input('Введіть число для пошуку першого індексу елемента в масиві: '))

# def binary_search(array: list, target: int) -> None:
#     left = 0
#     right = len(array) - 1
#     result = -1 
    
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             result = mid
#             right = mid - 1
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result

# target_index = binary_search(arr_numbers, target)

# print(f'Число {target} в масиві вперше зустрічається на індексі: {target_index}.' if target_index != -1
#       else f'Число {target} в масиві не знайдено!! Спробуйте ще раз.')

# Пошук першого входження елемента і останього входження елемента в масиві повернення результатів tuple 
# arr_numbers = sorted(random.randint(2, 9) for i in range(12))
# print(arr_numbers)
# target = int(input('Введіть число для пошуку його індексів першого\\останого входження в масив: '))

# def binary_search_first_last(array: list, target: int) -> tuple:

#     #  якщо не найдемо індекси першого\останого входження поверне -1
#     first = -1 
#     last = -1

#     # Пошук першого (індексу) входження в масив
#     left = 0
#     right = len(array) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             first = mid
#             right = mid - 1
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     # Пошук останього входження елемента в масив
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target:
#             last = mid
#             left = mid + 1
#         elif array[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     # повертаємо значення ідексів first, last
#     return first, last

# first_index, last_index = binary_search_first_last(arr_numbers, target)

# print(f'Число {target} вперше в масиві зустрічається на позиції: {first_index}, востаннє на позиції: {last_index}' if first_index != -1 and last_index != -1
#       else f'Число {target} в масиві не знайдене! Спробуйте ще раз...')

# a1 = [1, 2, 3, 5, 4]
# a2 = [5, 6, 7]
# b1 = a1 + a2
# print(b1)

