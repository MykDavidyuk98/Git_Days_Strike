# 1
import random


# 4 Видалення всіх входжень заданого елемента
# Видали зі списку всі елементи, що дорівнюють заданому значенню.

# 5 Зворотній порядок
# Створи новий список, елементи якого розташовані у зворотному порядку.

# 6 Об'єднання двох списків
# Об'єднай два списки в один.

# 7 Перевірка наявності елемента
# Перевір, чи є певний елемент у списку.

# 8 Видалення дублікатів
# Створи новий список без повторюваних елементів (залиш тільки унікальні значення).

# 9 Зсув елементів вправо
# Зсунь елементи списку на одну позицію вправо (останній стає першим).

# 10 Сортування списку
# Відсортуй список за зростанням та спаданням.





# arr_numbers = [random.randint(2, 10) for x in range(5)]
# print(arr_numbers)
# print(sum(arr_numbers))

# sum_arr = 0
# for x in arr_numbers:
#     sum_arr += x
# print(sum_arr)

# num_list = []
# for x in range(5):
#     number = int(input(f"Введіть {x+1}ше число для списку: "))
#     num_list.append(number)

# print(num_list)
# print(sum(num_list))

# 2
# Пошук найбільшого та найменшого елемента
# Знайди найбільший і найменший елемент у списку.

# num_list = [random.randint(2,10) for x in range (10)]
# print(num_list)

# max_num = num_list[0]
# min_num = num_list[0]
# for x in num_list:

#     if max_num < x:
#         max_num = x
    
#     if min_num > x:
#         min_num = x
    
# print(max_num)
# print(min_num)

# # Alternate option 
# print(max(num_list))
# print(min(num_list))

# 3
# Підрахунок кількості входжень елемента
# Порахуй, скільки разів заданий елемент зустрічається у списку.

# arr_numbers = [random.randint(2,11) for x in range(11)]
# print(arr_numbers)

# # count_num = int(input('Введіть число для пошуку його кількості в списку: '))
# # print(arr_numbers.count(count_num))

# found_num = int(input('Введіть число для пошуку його кількості в списку: '))
# count_num = 0
# for x in arr_numbers:
#     if x == found_num:
#         count_num += 1

# print(count_num)

# 4 Видалення всіх входжень заданого елемента
# Видали зі списку всі елементи, що дорівнюють заданому значенню.

# arr_num = [random.randint(1,10) for x in range(8)]
# print(arr_num)

# del_num = int(input('Введіть елемент який потрібно прибрати зі списку: '))

# # arr_num = [x for x in arr_num if x != del_num]
# # print(arr_num)

# # Alternate option:
# for x in arr_num:
#     if x == del_num:
#         arr_num.remove(del_num)

# print(arr_num)


# 5 Зворотній порядок
# Створи новий список, елементи якого розташовані у зворотному порядку.

# list_len = int(input("Задайте довжину списку: "))
# arr_num = [random.randint(1,10) for x in range(list_len)]
# print(arr_num)

# arr_num = sorted(arr_num, reverse = True)
# print(arr_num)

# arr_num = [random.randint(2,11) for x in range(11)]
# print(arr_num)
# # arr_num.reverse()
# # print(arr_num)

# # Alternate option 
# print(arr_num[::-1])

# 6 Об'єднання двох списків
# arr_num1 = [random.randint(2, 5) for x in range(5)]
# arr_num2 = [random.randint(6,10) for x in range(5)]
# print(arr_num1)
# print(arr_num2)
# sum_list = arr_num1 + arr_num2 
# print(sum_list)

# 7 Перевірка наявності елемента
# Перевір, чи є певний елемент у списку.

# arr_num = [random.randint(2, 13) for x in range(13)]
# print(arr_num)

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for x in range(N-1):

#         for k in range(N-1-x):

#             if arr_num[k] > arr_num[k+1]:
#                 arr_num[k], arr_num[k+1] = arr_num[k+1], arr_num[k]

# bubble_sort(arr_num)
# print(arr_num)

# found_num = int(input('Введіть елемент для пошуку в списку: '))

# print(arr_num.index(found_num))

