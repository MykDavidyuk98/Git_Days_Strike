import math
import random
import requests

# def foo(x: str, y: int) -> str:  
#   result = x 
#   for i in range (y -1):
#     result += x
#   return result

# y = foo(2, 5)
# print(y)
# y = foo('ma', 2)
# print(y)

# def foo(x, y, z = 0): 
#     return 100*x + 10*y +1*z
# t = foo(1,2,3)
# print(foo(1,2,3,))
# print(foo(z = 1, x = 2, y =3))
# print(foo(1,2))                     # параметр z використовує значення по замовчуванню

# def bar(args):
#     for arg in args:
#         print("bar arg = ", arg)
    
# bar([1,2,3])

#  DRY — Don't Repeat Yourself
# Якщо ти бачиш однакові або дуже схожі фрагменти — винеси їх у функцію або змінну.
# 🔸 Мета: зменшити дублювання, полегшити зміни в коді.
# ✅ Приклад (DRY):

# def greet (name):
#     print(f'Hello {name}')
# greet('Sacha')
# greet('Olia')

# 💧 WET — Write Everything Twice (або We Enjoy Typing)
# Повторюваний код, копіювання логіки без узагальнення.
# ❌ Приклад (WET):
# print('Hello Anna')
# print('Hello Kolia')

# Висновок:
# DRY = добре (структуровано, підтримувано)
# WET = погано (багато дублювання, складно змінювати)

# task 1 GPT na DRY, WET у коді
# def print_user (user: str, age: int, city: str):
#     print(f'User: {user}\nAge: {age}\nCity: {city}')
# print_user('Anna', 22, 'Lviv\n')
# print_user('Oleh', 30, 'Kyiv\n')
# print_user('Marta', 19, 'Odesa')

# кінець
# def countdown(timer = 3):
#     if timer == 0:
#         print('Engine start')
#     else:
#         print(timer)
#         countdown(timer -1)

# countdown(10)

# task 2 GPT 
# Напиши три функції: a(), b(), c()
# - Функція a() викликає b()
# - Функція b() викликає c()
# - Функція c() просто виводить "Hello from C"
# Виклич функцію a()

# def c ():
#   print('Hello from C')
# def b():
#   c()
# def a():
#   b()
# a()

# task 3 GPT 
# Напиши рекурсивну функцію print_down(n), яка виводить числа від n до 1
# і після 1 виводить "Готово!"
# Приклад: print_down(3) -> 3 2 1 Готово!

# def print_down (n):
#     if n != 1:
#         if n > 1:
#             print(n, ' ', end='')
#             print_down (n -1)
#         else:
#             print(n, ' ', end='')
#             print_down(n + 1)
#     else:
#         print(f'{n} Готово', end='!')
# print_down(-10)

# оператор пас(pass) не виконує жодних дій в інструкції, тобто він використовується коли тіло функції не має інструкцій 
# def fun_05 (a: int, b: int, c: int):
#     return (a+b+c)/y
# x1 = (2, 3, 4)
# x2 = [5, 6, 7]
# y = len(x1)
# print(fun_05(*x1))
# y = len(x2)
# print(fun_05(*x2))

# def func_6 (a, b, c):
#     s = a + b + c
#     return math.sqrt(s)

# task 1 st107 def 
# def cone_size ():
#     radius = 3
#     height = 5
#     volume = (1 / 3) * math.pi * radius ** 2 * height
#     return volume
# print(cone_size ())

# task 2 st107 def
# def triangle (a: int, b: int):
#     c = math.sqrt(a**2 + b**2)
#     return print(f'Параметр прямокутного трикутника = {c + a + b}')
# triangle(2, 9)
# triangle(6,10)
# def circle (r: int):
#     S = math.pi * r**2
#     return f'Площа кола з радіусом {r} = {S}'
# print(circle(5))

# def calculate_shapes (a: int, b: int, r: int):
#     c = math.sqrt(a**2 + b**2)
#     S = math.pi * pow(r, 2)
#     print(f'Параметр прямокутного трикутника = {c + a + b}\nПлоща кола з радіусом {r} = {S}')
# calculate_shapes(2, 5, 6)
# calculate_shapes(5, 6, 10)

# task 3 st107 def
# def calc(a: int, b: int, c:int, d: int):
#     sum = a*b - c/d
#     return sum
# num_list = [3, 5, 2, 7]
# num_tuple = (4, 1, 5, 6)
# print(f'Обчислення виразу для значень списку: {num_list}, буде дорівнювати {calc(*num_list)}')
# print(f'Обчислення виразу для значень кортежу: {num_tuple}, буде дорівнювати {calc(*num_tuple)}')
# for j in range(1,6):
#     print('*'*j,)