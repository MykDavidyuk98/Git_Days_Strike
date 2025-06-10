import math
import random

from accessify import private, protected


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


# arr_word = ['kiwi', 'banana', 'fig', 'apple']

# def selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i

#         for k in range(i + 1, N):

#             if len(array[k]) < len(array[min_index]):
#                 min_index = k

#         array[i], array[min_index] = array[min_index], array[i]

# print(arr_word)
# selection_sort(arr_word)
# print(arr_word)

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

# arr_number = [10, 4, 2, 7, 1, 98, 23]

# def selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i

#         for k in range(i+1, N):
#             if array[k] > array[min_index]:
#                 min_index = k
#         array[i], array[min_index] = array[min_index], array[i]

# print(arr_number)
# selection_sort(arr_number)
# print(arr_number)

# arr_words = ['grape', 'banana', 'fig', 'kiwi', 'apple']

# def count_vowels(word: str) -> int:
#     vowels = 'aeoiuAEOIU'
#     return sum(1 for char in word if char in vowels)

# def selection_sort(array: list, key = lambda x: x):
#     N = len(array)

#     for i in range(N):
#         min_index = i 

#         for k in range(i+1, N):
#             if key(array[k]) < key(array[min_index]):
#                 min_index = k
        
#         array[i], array[min_index] = array[min_index], array[i]

# print(arr_words)
# selection_sort(arr_words, key = count_vowels)
# print(arr_words)


# arr_num = [5, 2, 4, 1, 3]

# def selection_sort(array: list) -> None:
#     N = len(array)
#     swap_count = 0

#     for i in range(N):
#         min_index = i 

#         for k in range(i+1, N):
#             if array[k] < array[min_index]:
#                 min_index = k

#         if min_index != i:
#             array[i], array[min_index] = array[min_index], array[i]
#             swap_count += 1

#     return swap_count

# print(arr_num)
# res = selection_sort(arr_num)
# print(arr_num, res)

# 1
# class Point:

#     a1 = 21.5
#     a2 = 4
#     a3 = 37
#     print(f'Результат - {a1 + a2 + a3}')
#     b1 = 'Київ'
#     b2 = '-21'
#     print(f'Результат - {b1 + b2}')
#     c1 = 48
#     c2 = 5
#     print(f'Результат - {c1 * c2}')
#     c1_1 = '7'
#     if type(c1_1) == str:
#         c1_1 = int(c1_1)
#     c1_2 = 'файл'
#     print(f'Результат - {c1_1 * c1_2}')

# ob1 = Point()

# class Point:

#     def __init__(self):
#         a1, a2, a3 = 21.5, 4, 37
#         print(f'Операція "+" над int: {a1}, {a2}, {a3} - {a1 + a2 + a3}')

#         b1, b2 = 'Київ', '-21'
#         print(f'Операція "+" над str: {b1}, {b2} - {b1 + b2}')

#         c1, c2 = 48, 5
#         print(f'Операція "*" над int: {c1}, {c2} - {c1 * c2}')

#         d1, d2 = '7', 'файл'
#         d1 = int(d1) if isinstance(d1, str) else d1
#         print(f'Операція "*" над строками: {d1}, {d2} - {d1 * d2}')

# ob1 = Point()


# 2
# class K_01:

#     def __init__(self, a1: list):
#         self.p1 = a1
    
#     def func1(self):
#         return sum(self.p1)
    
#     def func2(self):
#         res = 0
        
#         for i in range(len(self.p1)):
#             res += self.p1[i]
#         return res

# class K_02:

#     def __init__(self, a1: list):
#         self.p1 = a1
    
#     def func1(self):
#         return max(self.p1)
    
#     def func2(self):
#         max_num = 0
#         for i in range(1, len(self.p1)):
#             if max_num < self.p1[i]:
#                 max_num = self.p1[i]
#         return max_num


# arr_numbers = [random.randint(2, 10) for i in range(10)]
# print(arr_numbers)
# ob1 = K_01(arr_numbers)
# print(ob1.func1())
# print(ob1.func2())
# ob2 = K_02(arr_numbers)
# print(ob2.func1())
# print(ob2.func2())

# 3
# class Common:
    
#     def __init__(self, a1: list):
#         self.p1 = a1
    
#     def func(self):
#         raise NotImplementedError('Цей метод має бути перевизначений у підкласі (K_01 / K_02)')

# class K_01(Common):
    
#     def func(self):
#         res = 1

#         for i in range(len(self.p1)):
#             res *= self.p1[i]
#         return res

# class K_02(Common):

#     def func(self):
#         res = 0

#         for i in range(len(self.p1)):
#             res += self.p1[i]
#         return res

# arr_numbers = [random.randint(1, 15) for i in range(5)]
# print(arr_numbers)
# if arr_numbers[0] > arr_numbers[-1]:
#     ob1 = K_01(arr_numbers)
#     print(ob1.func())
# else:
#     ob1 = K_02(arr_numbers)
#     print(ob1.func())
# ob1 = Common(arr_numbers)
# print(ob1.func())

# 4
# class Point:

#     def __init__(self, a1, a2):
#         self.p1 = a1
#         self.p2 = a2

#     def __add__(self, a2):
#         self.p1 = self.p1 + a2
#         return self.p1

# ob1 = Point(143.5, 32.4)
# print(ob1 + ob1.p2)
# ob1 = Point('ай', "фон")
# print(ob1 + ob1.p2)

# 5
# Створи клас Box, який має одне поле — weight (вага коробки). 
# Реалізуй методи __gt__ (більше) та __eq__ (дорівнює), щоб можна було порівнювати об'єкти Box між собою:
# 📋 Вимоги:
# Якщо одна коробка важча — повертається True для операції >.
# Якщо дві коробки мають однакову вагу — == має повертати True.

# box1 = Box(10)
# box2 = Box(7)
# box3 = Box(10)

# print(box1 > box2)   # True
# print(box1 == box3)  # True
# print(box2 == box3)  # False


# class Box: 

#     def __init__(self, weight):
#         self.p1 = weight
    
#     def __gt__(self, a1):
#         return self.p1 > a1.p1
       
        
#     def __eq__(self, a1):
#         return self.p1 == a1.p1

# ob1 = Box(16)
# ob2 = Box(12)
# print(ob1 > ob2)
# print(ob1 == ob2)
# ob3 = Box(3)
# ob4 = Box(3)
# print(ob3 == ob4)
# print(ob3 > ob4)
# print(ob4 > ob3)
        
# x = 5
# print(isinstance(x, (float, int, str)))