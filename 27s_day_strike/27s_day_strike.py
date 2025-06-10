import math
import random
import re

# def string_operation () -> None:
#     a = 'Рядок є незмінним'
#     b = "типом данних"
#     C = ' '.join((a, b))
#     print(C, f'\n{len(C)}')
#     some_text = C[8:17]
#     print(some_text)
#     C = C.replace(some_text, 'ЗМІННИМ')
#     print(C)
# string_operation()


# some_text = ('кількість', "входжень")
# other_text = ('підрядка', "у рядок")
# whole_text = some_text + other_text
# print(whole_text)
# whole_text = ', '.join(whole_text)
# print(whole_text)
# some_count = whole_text.count('підрядка')
# print(some_count)
# print(ord('к'))


# def print_some_text() -> None:
#     a = 'рядок є незмінним типом данних'
#     print(a.capitalize())
#     print(ord(a[8]))
#     print(a.count('м'))
#     print(a.find('типом'))
#     print(len(a[8:17]))
# print_some_text()


# def print_some_text() -> None:
#     a = 'Операційна'
#     b = 'система'
#     print(len(a))
#     print(len(b))
#     c = a + ' ' + b
#     print(c)
#     print(len(c))
# print_some_text()


# def print_some_text() -> None:
#     a = 'Принтер LM Laser P1006'
#     a = a.replace('LM Laser', 'HP laserJet')
#     print(a)
# print_some_text()


# def print_some_text() -> None:
#     a = 'Рим - столиця Італії, Париж - столиця Франції'
#     print(ord('м'))
#     print(a.count('столиця'))
# print_some_text()


# def print_some_text() -> None:
#     a = 'microsoft Word'
#     a = a.replace('m', 'M')
#     print(a)
#     print(a.count('o'))
#     print(ord(a[5]))
#     print(a[5])
# print_some_text()


# def print_some_text() -> None:
#     a = 'Інструкція для користувача'
#     print(a)
#     a = a.replace('користувача', 'вчителя')
#     print(a)
#     print(a.find('для'))
# print_some_text()


# array = [27, 3, 12, 22, 37, 8]
# def print_arr_actions(arr: list) -> None:
#     print(max(arr))
#     arr.pop(2)
#     print(arr)
#     print(sorted(arr))
#     print(arr)
#     arr.insert(4, 5)
#     arr[1] = 10
#     print(arr)
# print_arr_actions(array)


# array_1 = ['Python розробив', '1991']
# array_2 = ['Гвідо ван']
# def some_arr_actions(arr1: list, arr2: list) -> None:
#     # full_arr = arr1 + arr2
#     arr1.insert(0, 'Мову')
#     arr1.insert(2, 'у')
#     arr2.insert(0, 'році')
#     arr2.append('Россум')
#     full_arr = arr1 + arr2
#     print(full_arr)
#     print(' '.join(full_arr))
# some_arr_actions(array_1, array_2)


# array = [4, 6, 13, 9, 5, 16, 11]
# def some_arr_actions (arr: list) -> int:
#     N = len(arr)
#     sum_numbers = 0
#     for i in range(N):
#         if arr[i] > 6:
#             arr[i] *= 2
#             print(arr[i])
#             sum_numbers += arr[i]
#     return sum_numbers
# sum_num_arr = some_arr_actions(array)
# print(f'Сума чисел більших за 6 в масиві - {sum_num_arr}')


# array = [13, 19, 11, 7, 18]
# array.pop(1)
# print(array)
# print(max(array))


# array_num = [21, 40, 7, 10, 12]
# array_num.insert(1, 10)
# new_array = sorted(array_num)
# print(array_num)
# print(new_array)


# arr_numbers = [9, 2, 5, 6]
# arr_numbers[0] = 12
# new_array = sorted(arr_numbers)
# print(arr_numbers, f'\n{new_array}')


# array_words = ['В.Глушков', 'учений України']
# array_words.insert(1, "- великий" )
# array_words = ' '.join(array_words)
# print(array_words)


# array1 = ['Мова', "Pascal"]
# array2 = ['- це мова', "процедурного програмування"]
# full_array = array1 + array2
# full_array = ' '.join(full_array)
# print(full_array)
# print(type(full_array))


# arr_numbers = [5, 7, 8, 12, 4]

# def sum_element(arr: list) -> int:
#     sum_elements = 0
#     N = len(arr)

#     for i in range(N):
#         if arr[i] > 5:
#             sum_elements += arr[i]
#     return sum_elements

# sum = sum_element(arr_numbers)
# print(f'Сума елементів > 5 в масиві: {sum}')

# 1
# arr_words = ['яблуко', "банан", "вишня"]
# arr_words[1] = 'груша'
# print(arr_words)

# 2
# Виведи перші три елементи зі списку [10, 20, 30, 40, 50].
# arr_numbers = [10, 20, 30, 40, 50]
# print(arr_numbers[0:3:1])

# або
# print(arr_numbers[:3])

# 3
# Об'єднай два списки: [1, 2, 3] і [4, 5, 6] в один.
# arr1 = [1, 2, 3]
# arr2 = [4, 5, 6]
# full_arr = arr1 + arr2
# print(full_arr)

# 4
# Перетвори рядок 'python' у список символів.
# some_str = 'python'
# some_arr = list(some_str)
# print(some_arr)

# 5
# Виведи максимальне та мінімальне число зі списку [15, 3, 9, 27, 6].
# arr_numbers = [15, 3, 9, 27, 6]
# max_num, min_num = max(arr_numbers), min(arr_numbers)
# print(max_num, min_num)

# 6
# Додай елемент 'кіт' до списку тварин ['собака', 'папуга'].
# arr_animals = ['собака', "папуга"]
# arr_animals.append('кіт')
# print(arr_animals)

# 7
# Встав елемент 'місто' у список ['село', 'область'] на позицію 1.
# arr_locality = ['село', "область"]
# arr_locality.insert(0, 'місто')
# print(arr_locality)

# 8
# Розшир список ['a', 'b'] елементами з іншого списку ['c', 'd'].
# arr1 = ['a', 'b']
# arr2 = ['c', 'b']
# arr1.extend(arr2)
# print(arr1)

# 9
# Видали останній елемент зі списку [1, 2, 3, 4].
# arr_numbers = [1, 2, 3, 4]
# arr_numbers.pop(3)
# print(arr_numbers)

# 10
# Видали значення 5 зі списку [2, 5, 7, 5, 1] (тільки першу появу).
# arr_numbers = [2, 5, 7, 5, 1]
# arr_numbers.remove(5)
# print(arr_numbers)

# 11 
# Очисти повністю список [10, 20, 30].
# arr_numbers = [10, 20, 30]
# arr_numbers.clear()
# print(arr_numbers)

# 12
# Порахуйте, скільки разів число 3 зустрічається у списку [3, 1, 3, 5, 3, 7].
# arr_numbers = [3, 1, 3, 5, 3, 7]
# count_3 = arr_numbers.count(3)
# print(count_3)

# 13
# Знайди індекс першої появи елемента 'сніг' у списку ['дощ', 'сніг', 'сонце'].
# arr_words = ['дощ', "сніг", "сонце"]
# word_index = arr_words.index('сніг')
# print(word_index)

# 14
# Відсортуй список [5, 2, 9, 1] на місці (зміни його).
# arr_numbers = [5, 2, 9, 1]
# arr_numbers.sort()
# print(arr_numbers)

# 15
# Створи нову копію відсортованого списку [10, 3, 6], не змінюючи початковий.
# arr_numbers = [10, 3, 6]
# arr_num_sort = sorted(arr_numbers.copy())
# print(arr_num_sort)
# print(id(arr_num_sort))
# print(id(arr_numbers))

# 16
# Випадково вибери один елемент зі списку кольорів.
# arr_colors = ['yellow', 'red', 'green', 'purple', 'blue']
# random_el = random.choice(arr_colors)
# print(random_el)

# 17
# Створи новий список із 3 випадкових чисел з діапазону [1, 10].
# arr_numbers = random.sample(range(1, 11), 3)
# print(*arr_numbers)

# 18
# Згенеруй список із 10 чисел від 1 до 10, а потім створити новий, в якому кожне число буде подвоєне.
# arr_numbers = [x for x in range(1,11)]
# new_arr = [x*2 for x in arr_numbers]
# print(arr_numbers)
# print(new_arr)

# 19
# Дано список цілих чисел. Створи новий список, який містить тільки парні числа.
# arr_numbers = [x for x in range(16)]
# new_arr_even = [x for x in arr_numbers if x % 2 == 0]
# print(new_arr_even)

# 20
# Створи список зі слів, введених користувачем (через input()), і виведи їх у зворотному порядку.
# arr_words = [str(input('Введіть слово: '))for i in range (5)]
# print(arr_words)
# print(sorted(arr_words, reverse=True))

# a = 14, 107, 'Київ', "Театральна", 21 
# print(a[2])
# print(a[:3])
# print(len(a))
# print(a.count(107))
# print(a.index('Театральна'))

# a = range(2, 9)
# # print(a[2])
# print(a[2:6])

# a = range(3, 18, 2)
# print(a)
# a = list(a)
# print(a)
# a = tuple(a)
# print(a)
# print(a[5])
# a = range(3, 18, 2)
# print(a)
# print(len(a))
# print(sum(a))

# a = 2, 3, 4, 12, 12, 5, 2, 13, 13, 13
# a = set(a)
# print(a)
# a = set([3, 4, 7, 7])
# print(a)
# b = a.union([5, 67, 13])
# print(a)
# print(b)
# a = {a for a in [2, 2, 2, 5, 5, 6 ,7]}
# print(a)
# print(len(a))

# a = set([2, 4, 6, 8])
# b = set([10, 12, 14, 16])
# print(a == b)
# c = a.union(b)
# print(c)
# c.add(18)
# print(c)
# print(len(c))
# print(12 in c)
# # print(sum(b))
# sum = 0
# for i in b:
#     sum += i
# print(sum)

# a = 'Інформатика', "вивчається", "у", 5, "класі"
# print(len(a))
# print(a[3])

# a = 21, 16, "файл", 16, "блок", 16
# print(a.count(16))
# print(a.index('блок'))
# print(a[1:4])

# a = range(5, 15)
# print(*a)
# a = list(a)
# print(a)
# print(len(a))

# b = list([5, 'torf', 'some_text', (3, 5)])
# print(b)
# print(type(b))

# a = range(12, 29, 2)
# print(*a)
# a = tuple(a)
# print(a)
# print(sum(a))

# # alternate option
# sum_tuple = 0
# for i in a:
#     sum_tuple += i
# print(sum_tuple)

# a = set([1, 2, 3])
# b = set([2, 4, 6])
# c = a.union(b)
# print(c)
# c.add(int('7'))
# print(c)

set1 = set([5, 7, 8])
set2 = set([12, 14, 16, 18])
print(len(set1))
print(len(set2))
set3 = set1 | set2
print(set3)
sum_set = sum(set3)
print(sum_set)