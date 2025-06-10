import math
import random

# def some_math_actions (a, b = 5) -> float:
#     if a > b:
#         result = a*pow(b, 2) - 2*a
#         return float(result)
#     else:
#         result = a / b
#         return float(result)

# result = some_math_actions(6)
# print(result)
# result = some_math_actions(4)
# print(result)
# result = some_math_actions(5, 10)
# print(result)


# arr_num = [1, 3, 5, 7, 9]
# tuple_numbers = (6, 8, 10)
# def sum_numbers (*args) -> int:
#     total  = 0
#     for i in args:
#         total  += i
#     return total 
# print(sum_numbers(*arr_num))
# print(sum_numbers(*tuple_numbers))

# # with no args
# a1 = lambda: 3/7 + 5*8/3
# print(a1())

# # with args 
# a2 = lambda x, y: (2*x) + (x/y)
# print(a2(5, 10))
# a3 = lambda x, y: (3*x + 5) / (y - 2)
# print(a3(5, 7))

# tuple_numbers = 3, 7
# list_numbers = [4, 6, 7, 9, 10]

# def some_math_actions(a, b = 5, *args) -> int:
#     sum_numbers = a * b 
#     for i in args:
#         sum_numbers *= i
#     return sum_numbers

# print(some_math_actions(tuple_numbers[0], tuple_numbers[1]))
# print(some_math_actions(*list_numbers))

# Створи функцію, яка приймає два обов’язкові параметри a і b та повертає їх суму.
# Порада: використай просту def-функцію.

# 1
# def sum_numbers(a: int, b: int) -> int:
#     sum_value = a + b
#     return sum_value

# print(sum_numbers(5, 10))

# 2
# Напиши функцію, яка приймає один обов’язковий параметр x і один необов’язковий параметр y=2. Поверни x у степені y.

# def x_pow_y(x: int, y = 2) -> int:
#     sum_value = pow(x, y)
#     return sum_value
# print(x_pow_y(5))
# print(x_pow_y(5, 3))

# 3
# Створи функцію, яка приймає будь-яку кількість чисел (*args) і повертає їх середнє значення.

# def averege_sum(*args) -> float:
#     sum_value = sum(args) / len(args)
#     return float(sum_value)
# a = 2, 3, 5
# print(averege_sum(*a))


# 4
# Напиши функцію з 1 обов’язковим, 1 необов’язковим параметром (mult=1) і довільною кількістю чисел. 
# Поверни суму всіх чисел, помножену на mult.
# Приклад: func(2, 10, 1, 2, 3) → (1+2+3)*10 = 60.

# def multiply_nubers(a, mult = 1, *args) -> int:
#     sum_numbers = (a + sum(args)) * mult
#     return sum_numbers

# arr_numbers = [2, 10, 3, 5]
# print(multiply_nubers(*arr_numbers))

# 5
# Створи анонімну функцію, яка обчислює вираз 3x + 5 і застосуй її до списку [1, 2, 3, 4] через map.
# arr_numbers = [1, 2, 3, 4]
# new_list = list(map(lambda x: 3*x + 5, arr_numbers))
# print(new_list)


# 6
# Реалізуй функцію, яка приймає ключові аргументи **kwargs і повертає список ключів, де значення більше за 10.
# Приклад: func(a=5, b=20, c=15) → ['b', 'c']

# def selection_sot(array: list) -> None:

#     for i in range(len(array)):
#         min = i

#         for k in range(min, len(array)):
#             if array[min] > array[k]:
#                 min = k
#         array[i], array[min] = array[min], array[i]

#     return array

# arr_num = [1, 10, 15, 9, 5, 3]
# print(arr_num)

# new_sorted_arr = selection_sot(arr_num)
# print(new_sorted_arr)
    
# arr = [-5, 1, 10, 5, 3, 18, 23, 20]

# def selection_sort(array: list) -> None:
#     N = len(array)
    
#     for i in range(N-1):
#         min_value = array[i]
#         min_index = i
#         for j in range(i+1, N):
#             if min_value > array[j]:
#                 min_value = array[j]
#                 min_index = j

# arr = [1, 5, 2, 10, 8, 25, 18]
# def selection_sort(array: list) -> None:
#     N = len(array)
#     for i in range(N):
#         min_index = i
#         for k in range(i+1, N):
#             if array[k] < array[min_index]:
#                 min_index = k
#         array[min_index], array[i] = array[i], array[min_index]

# selection_sort(arr)
# print(arr)


# def selection_sort(array: list) -> None:
#     N = len(array)
#     for i in range(N):
#         min_index = i
#         for k in range(i+1, N):
#             if array[min_index] > array[k]:
#                 min_index = k
#         array[min_index], array[i] = array[i], array[min_index]

# arr_numbers = [1, 10, 5, 102, 58, 34]
# selection_sort(arr_numbers)
# print(arr_numbers)

# def reverse_selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i
#         for k in range(i+1, N):
#             if array[min_index] > array[k]:
#                 min_index = k
#         array[min_index], array[i] = array[i], array[min_index]

# arr_numbers = [1, 10, 2, 34, 18, 20, 24]
# reverse_selection_sort(arr_numbers)
# print(arr_numbers)

# # 3
# arr_words = ["banana", "apple", "cherry"]

# def selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i
#         for k in range(i+1, N):
#             if array[min_index] > array[k]:
#                 min_index = k
#         array[min_index], array[i] = array[i], array[min_index]

# selection_sort(arr_words)
# print(arr_words)


# # 4
# age_list = [{'age': 25}, {'age': 10}, {'age': 13}, {'age': 29}]

# def selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i
#         for k in range(i+1, N):
#             if array[min_index]['age'] > array[k]['age']:
#                 min_index = k
#         array[min_index], array[i] = array[i], array[min_index]

# selection_sort(age_list)
# print(age_list)


# 1
# arr_numbers = [1, 10, 2, 18, 39, 25]
# def insert_sort(array: list) -> None:
#     N = len(array)
    
#     for i in range(1, N):
#         k = i

#         while k > 0 and array[k] < array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# insert_sort(arr_numbers)
# print(arr_numbers)

# 2
# arr = ["pear", "apple", "orange", "banana"]
# def insert_sort(array: list) -> None:
#     N = len(array)

#     for i in range(1, N):
#         k = i
#         while k > 0 and array[k] < array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# insert_sort(arr)
# print(arr)


# # 3
# # Сортування від більшого до меншого
# arr_numbers = [1, 5, 2, 10, 15, 13, 20]
# def insert_sort(array: list) -> None:
#     N = len(array)

#     for i in range(1, N):

#         # задаємо тимчасову перемінну для внутрішнього сортування списку
#         k = i           

#         while k > 0 and array[k] > array[k-1]:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# insert_sort(arr_numbers)
# print(arr_numbers)
        
# # 4
# arr_dict = [{'score': 88}, {'score': 70}, {'score': 92}, {'score': 65}]

# def insert_sort(array: list) -> None:
#     N = len(array)

#     for i in range (1, N):
#         k = i

#         while k > 0 and array[k]['score'] < array[k-1]['score']:
#             array[k], array[k-1] = array[k-1], array[k]
#             k -= 1

# insert_sort(arr_dict)
# print(arr_dict)

# bubble_sort 
# 1

# arr_numbers = [1, 5, 9, 2, 3, 11, 8]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N - 1):
#         k = i

#         for k in range(N-1-i):
#             if array[k+1] < array[k]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(arr_numbers)
# print(arr_numbers)

# 2
# arr_words = ["grape", "apple", "banana", "cherry"]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N-1):
#         k = i 

#         for k in range(N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(arr_words)
# print(arr_words)
            
# 3
# Сортування чисел за спаданням

# arr_numbers = [1, 6, 3, 10, 20, 35, 28]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N - 1):
#         k = i

#         for k in range(N-1-i):
#             if array[k] < array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(arr_numbers)
# print(arr_numbers)

# 4
# Сортування словників за значенням ключа 'value'
# arr_dict = [{'value': 12}, {'value': 5}, {'value': 20}, {'value': 3}]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N -1):
#         k = i

#         for k in range(N-1-i):
#             if array[k]['value'] > array[k+1]['value']:
#                 array[k], array[k+1] = array[k+1], array[k]

# bubble_sort(arr_dict)
# print(arr_dict)


# Умова: Знайди значення за ключем "name" у словнику.
# 1
# person = {'name': 'Anna', 'age': 25, 'city': 'Kyiv'}
# print(person['name'])


# Умова: Перевір, чи є ключ "email" у словнику. Якщо нема — виведи "Немає такого ключа".
# 2
# user = {'username': 'admin', 'id': 101}
# print(f'Ключ "email" є в словнику{user}' if 'email' in user
#       else f'Такого ключа немає!')

# Умова: Є список словників. Знайди словник, у якому "score" найбільший.
# students = [
#     {'name': 'Olga', 'score': 78},
#     {'name': 'Ivan', 'score': 85},
#     {'name': 'Dmytro', 'score': 91}
# ]

# print(max(students, key=lambda student: student['score']))

# ✅ Завдання 4
# Умова: Є словник, у якому значення — це вкладені словники. Знайди ім’я користувача з найменшим віком.

# users = {
#     "u1": {"name": "Ivan", "age": 33},
#     "u2": {"name": "Svitlana", "age": 27},
#     "u3": {"name": "Andrii", "age": 41}
# }
# # Очікувано: "Svitlana"

# users = {
#     'u1': {'name': 'Ivan', 'age': 33},
#     'u2': {'name': 'Svitlana', 'age': 27},
#     'u3': {'name': 'Andrii', 'age': 41}  
# }

# print(min(users.values(), key=lambda young: young['age']))

# Умова: Є список словників з полем 'name'. Відсортуй список за зростанням довжини імені.

# users = [
#     {"name": "Olena", "age": 22},
#     {"name": "Ihor", "age": 35},
#     {"name": "Anastasiia", "age": 19}
# ]

# print(sorted(users, key=lambda lenght: len(lenght['name'])))

# Умова: У словнику зберігається інформація про користувачів і кількість їхніх повідомлень. Знайди користувача з найбільшою активністю.

# a = lambda x = 4: 3*x + 1
# print(a(5))

# b = lambda y: y % 2 == 0
# print(f'Число парне' if b(6) else 'Число не парне!')


# 1
# Є два набори товарів у кошиках двох покупців. Знайди товари, які купили обидва.

# basket1 = {'milk', 'bread', 'apple'}
# basket2 = {'bread', 'apple', 'juice'}

# common = lambda x, y: x & y
# print(common(basket1, basket2))

# 2
# Є два списки студентів, які відвідали два різні факультативи. Знайди тих, хто був на обох.
# group1 = {'Oleg', 'Marta', 'Ivan', 'Nina'}
# group2 = {'Ivan', 'Marta', 'Dima', 'Andrii'}

# common_intersection = lambda x, y: x & y
# print(common_intersection(group1, group2))


# 3
# workers = {"w1": "Anna", "w2": "Petro", "w3": "Olha", "w4": "Nazar"}
# certified = {"w2", "w4", "w5"}

# # common = set(workers.keys()) & certified
# common = lambda x, y: set(x.keys()) & y
# common_list = common(workers, certified)
# result = [workers[workers_id] for workers_id in common_list]
# print(result)

# 1
# Є два набори книг у бібліотеках. Знайди книги, які є лише в першій бібліотеці.

# library1 = {'1984', 'Harry Potter', 'Dune', 'Moby Dick'}
# library2 = {'Dune', 'Moby Dick', 'Dracula'}

# print(library1 - library2)


# 2
# Є список запрошених гостей та тих, хто вже прийшов. Знайди, хто ще не з’явився.

# invited = {'Serhii', 'Kateryna', 'Oksana', 'Denys'}
# arrived = {'Oksana', 'Denys'}

# not_arrived = lambda x, y: x.difference(y)
# print(not_arrived(invited, arrived))


# 3
# У компанії є всі зареєстровані працівники та список тих, хто ще не пройшов інструктаж з техніки безпеки.
#  Знайди імена працівників, які ще не пройшли інструктаж:

# employees = {"e1": "Oksana", "e2": "Roman", "e3": "Ihor", "e4": "Vira"}
# trained = {"e2", "e4"}

# employees_keys_list = set(employees.keys())
# print(employees_keys_list)

# not_trained = lambda x, y: x -y
# new_list =  not_trained(employees_keys_list, trained)

# not_trained_names = [employees[names] for names in new_list]
# print(new_list)
# print(not_trained_names)

arr = [-5, 1, 10, 5, 3, 18, 23, 20]

def selection_sort(array: list) -> None:
    N = len(array)

    for i in range(N):
        min = i

        for k in range(min, N):
            if array[k] < array[min]:
                min = k
        array[i], array[min] = array[min], array[i]
    return array
            
new_arr = selection_sort(arr)
print(new_arr)












# def selection_sot(array: list) -> None:

#     for i in range(len(array)):
#         min = i

#         for k in range(min, len(array)):
#             if array[min] > array[k]:
#                 min = k
#         array[i], array[min] = array[min], array[i]

#     return array

# arr_num = [1, 10, 15, 9, 5, 3]
# print(arr_num)