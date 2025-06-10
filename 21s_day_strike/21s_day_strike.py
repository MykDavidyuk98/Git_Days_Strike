import math
import random
import time
print('')


# Користувач вводить два цілі числа — початок і кінець діапазону. 
# Потрібно знайти суму цифр усіх чисел у цьому діапазоні, які діляться на 3.
# Введіть початок: 10  
# Введіть кінець: 20
# Сума цифр чисел, кратних 3: 27

# start_num = int(input('Введіть початок діапазону (ціле число): '))
# stop_num = int(input('Введіть кінець діапазону (число буде включене до діапазону): ')) + 1
# sum_of_divisors_3 = 0
# for i in range(start_num, stop_num):
#     if i % 3 == 0:
#         print(i)
#         for k in str(i):
#             k = int(k)
#             sum_of_divisors_3 += k
# print(f'Сума цифр чисел, кратних 3: {sum_of_divisors_3}')


# Задача 2: Пошук найбільшого спільного дільника (НСД)
# Умова:
# Користувач вводить два додатні числа. Знайти їх найбільший спільний дільник (без використання math.gcd()).
# Реалізуй  швидкий алгоритм Евкліда за допомогою while.

# first_num = int(input('Введіть перше число: '))
# second_num = int(input('Введіть друге число: '))
# first_num_print = first_num
# second_num_print = second_num

# while first_num != second_num:
#     if first_num > second_num:
#         first_num -= second_num
#     else:
#         second_num -= first_num
# if first_num == second_num:
#     print(f'Найбільший спільний дільник чисел {first_num_print}, {second_num_print}: {first_num} ')


# def get_nod (first_num: int, second_num: int):
#     """Вичисляємо НСД для двух натуральних чисел first_num ,second_num
#         по швидкому алгоритму Евкліда
#         first_num - перше натуральне число
#         second_num - друге натуральне число 
#         return - значення НСД"""
#     if first_num < second_num:
#         first_num, second_num = second_num, first_num

#     while second_num != 0:
#         first_num, second_num = second_num, first_num % second_num
#     return first_num


# def test_nod(func):
#     # testcase #1
#     a = 28
#     b = 35 
#     res = func(a,b)
#     if res == 7:
#         print('#test1 - ok')
#     else:
#         print('#test1 - fail')

    
#     # testcase #2
#     a = 100
#     b = 1
#     res = func(a,b)
#     if res == 1:
#         print('#test2 - ok')
#     else:
#         print('#test2 - fail')


#     # testcase #2
#     a = 2
#     b = 10000000
#     st = time.time()
#     res = func(a, b)
#     et = time.time()
#     dt = et - st 
#     if res == 2 and dt < 1:
#         print('#test3 - ok')
#     else:
#         print('#test3 - fail')
# test_nod(get_nod)


# A = [random.randint(100,1000) for x in range(10)]
# A.append(111)
# A.append(222)
# count = 0
# for i in A:
#     s = str(i)
#     if len(s) == 3 and s[0] == s[1] == s[2]:
#         count += 1
#         print(i)
# print(A)
# print(f'всього чисел: {count}')


# mas = [random.randint(2,20) for i in range(10)]
# mas = sorted(mas)
# print(mas)
# target = int(input('Введіть шуканний елемент для повернення індексу: '))

# def binary_search(mas: list, target: int):
#     left = 0
#     right = len(mas) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if mas[mid] == target:
#             return mid
#         elif mas[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1

# found_index = binary_search(mas, target)
# print(f'Елемента {target} в списку немає!!!' if found_index == -1 else f'Елемент {target} має індекс: {found_index} в масиві')


# Список: [1, 2, 2, 2, 3, 4]
# Введено: 2
# Результат: Перше входження на позиції 1

# mas = [1, 2, 2, 2, 3, 4]
# target = 2

# def binary_search(array: list, target: int):
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
#     return - 1

# found_index = binary_search(mas, target)
# print(mas, '\n', f'У масиві шуканний елемент має індекс: {found_index}' if found_index != -1 else 'Масив не має шуканого елемента!!')


# Умова:
# Є список оцінок учня: [12, 8, 9, 10, 7, 11]
# Відсортуй список за зростанням за допомогою методу вставок.
# Очікувано: [7, 8, 9, 10, 11, 12]


# def binary_search (array: list):
#     N = len(array)
#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k] < array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1
#     return array

# A = [12, 8, 9, 10, 7, 11]
# B = binary_search(A)
# print(binary_search(A))

