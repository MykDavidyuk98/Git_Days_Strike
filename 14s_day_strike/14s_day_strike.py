import math
import random

# Перевірити, чи число парне
# Напиши функцію, яка приймає ціле число і повертає, чи є воно парним.

# Порахувати квадрат числа
# Створи функцію, яка приймає число та повертає його квадрат.

# Знайти середнє арифметичне трьох чисел
# Напиши функцію, яка приймає три числа і обчислює їх середнє.

# Вивести привітання для користувача
# Створи функцію, яка приймає ім’я користувача і виводить привітання у форматі: "Привіт, Ім’я!"


# Обчислити площу прямокутника
# Створи функцію, яка приймає довжину і ширину прямокутника та повертає його площу.
# def rectangle_area (a: int, b: int):
#     size = a * b
#     return size

# print(rectangle_area(5, 10))

# task 2 GPT 
# def even_number (some_number: int):
#     if some_number == 0:
#         print(f'Число {some_number} вводити не можна!!!')
#     elif some_number%2 == 0:
#         print(f'Число {some_number} ПАРНЕ!!!')
#     else:
#         print(f'Число {some_number} НЕПАРНЕ!!!')
# some_number = int(input('Введіть ціле число: '))
# even_number(some_number)

# task 3 GPT
# def square_of_num (some_number: int):
#     some_number *= some_number
#     return some_number
# # some_number = int('Введіть число')
# print(square_of_num(some_number = 5))

# task 4 
# def average_value (a: int, b: int, c: int):
#     return (a + b + c)/3
# A = [5, 5, 7]
# print(average_value(*A))

# task 5 GPT
# some_name = str(input('Введіть ваше імя: '))
# def greet_def (some_name: str):
#     return f'Привіт {some_name}!!!'
# print(greet_def (some_name))

# task 6 GPT 
# end_number = int(input('Введіть число для підрахуну суми від 1 до цього числа: '))
# sum_of_number = 0 
# for i in range(1, end_number + 1):
#     sum_of_number += i
# print(sum_of_number)

# task 7 GPT
# Вивести всі парні числа від 1 до N за допомогою for
# Умова: Створи програму, яка виводить усі парні числа від 1 до заданого числа N за допомогою циклу for.
# some_number = int(input("Введіть число"))
# for i in range(1, some_number +1):    
#     if i%2 == 0:
#         print(i)

# task 8 GPT
# some_number = int(input('Введіть число для визначення його факторіалу: '))
# fact_number = some_number
# while some_number == fact_number:
#     some_number = math.factorial(some_number)
# print(some_number)
    
# task 9 GPT
# some_numbers = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# while i < len(some_numbers):
#     if some_numbers[i] % 2 == 0:
#         print(some_numbers[i])
#         break
#     i += 1
 
# task 10 GPT
# Обчислення середнього значення до того, як число буде більше 100
# average_value = 0 
# i = 1
# while True:
#     some_number = int(input('Введіть число: '))
#     if some_number > 100:
#         break
#     average_value = (average_value + some_number)/i
#     print(average_value)
#     i += 1

# task 11 GPT 
# Обчислення суми всіх чисел від 1 до N за допомогою циклу while
# end_number = int(input('Ведіть число по яке потрібно вирахвати суму: '))
# sum_value = 0
# step = 1
# while step <= end_number:
#     sum_value += step
#     step += 1
# print(sum_value)

# task 12 GPT 
# Вивести всі непарні числа від 1 до N за допомогою циклу for
# last_number = int(input('Введіть крайне значення чисел : '))
# for i in range(1, last_number + 1):
#     if i % 2 != 0:
#         print(i)

# task 13 GPT 
# Вивести всі непарні числа від 1 до N за допомогою циклу for
# last_number = int(input('Введіть крайнє значення чисел: '))
# quantity_of_numbers = 1
# for i in range (1, last_number+1):
#     quantity_of_numbers *= i 
#     print(quantity_of_numbers)

# task 14 GPT 
# number = int(input('Введіть число: '))
# if number % 2 == 0 or number % (math.sqrt(number)) == 0:
#     print(f'число {number} НЕ просте!')
# else:
#     print(f'Число {number} ПРОСТЕ!')

# task 15 GPT 
# number = int(input('Введіть значення числа: '))
# first_number = number % 10
# second_number = number // 10
# sum_of_numbres = first_number + second_number
# print(sum_of_numbres)

# x = 5 
# print(type(x))
# print(hasattr(x, 'bit_length'))
# print(x.bit_length)
# print(dir(x))
# print(help(int))
# print(id(x))

# task 16GPT
# number = int(input("Введіть число: "))
# if number != 0:
#     if number%2 == 0:
#         if number < 0:
#             print(f'Число {number} Відємне і при цьому парне')
#         else:
#             print(f'Число {number} Додатнє і при цьому парне')
#     else:
#         if number < 0:
#             print(f'Число {number} Відємне і при цьому НЕпарне')
#         else:
#             print(f'Число {number} Додатнє і при цьому НЕпарне')
# else:
#     print(f'Число {number} це нуль, спробуйте з іншим числом')

# if number == 0:
#     print(f'Число {number} нуль, спробуйте з іншим числом')
# elif number > 0:
#     print(f'Число {number} ДОДАТНЄ та {"парне" if number % 2 == 0 else "непарне"}')
# else:
#     print(f'Число {number} Відємне та {"парне" if number % 2 == 0 else "непарне"}')

# task 17 GPT 
# Введіть число від 0 до 100.
# Виведіть:

# 90–100 → "Відмінно",

# 70–89 → "Добре",

# 50–69 → "Задовільно",

# Менше 50 → "Незадовільно".

# number = int(input('Введіть число від 0 до 100 : '))
# if not 0 <= number <= 100:
#     print('Спробуйте ще раз (від 0 до 100)')
# elif 90 <= number <= 100:
#     print('Відмінно')
# elif number >= 70:
#     print('Добре')
# elif number >= 50:
#     print('Задовільно')
# else:
#     print('Незадовільно')

# Визначення квадранта
# За координатами x і y визначити, в якому квадранті знаходиться точка (всі 4 варіанти).

# Максимум трьох чисел
# Введіть три різні числа. Знайдіть найбільше з них, використовуючи лише вкладені if.

# Завдання з датою
# Введіть число (день) і місяць.
# Якщо дата — 31 грудня, виведіть "Новий рік завтра!"
# Якщо 1 січня — "Новий рік був учора!"
# Інакше — просто дату у форматі: "Сьогодні: {день}.{місяць}".

# task 18 GPT
# x_coord = int(input('Введіть значення x: '))
# y_coord = int(input('Введіть значення y: '))

# if x_coord >= 0:
#     print(f'точка {x_coord}, {y_coord} знаходиться у {"першій" if y_coord >= 0 else "четвертій"} частині площини координат')
# else:
#     print(f'точка {x_coord}, {y_coord} знаходиться у {"другій" if y_coord >= 0 else "третій"} частині площини координат')

# task 19GPT
# first_number = int(input('Введіть перше число: '))
# second_number = int(input('Введіть друге число: '))
# third_number = int(input('Введіть третє число: '))
# if first_number > second_number:
#     print(f"З трьох чисел {first_number, second_number, third_number} найбільше: {first_number if first_number > third_number else third_number} ")
# else:
#     print(f"З трьох чисел {first_number, second_number, third_number} найбільше: {second_number if second_number > third_number else third_number}")
# max_number = max(first_number, second_number, third_number)
# print(f"З трьох чисел найбільше: {max(first_number, second_number, third_number)}")

# task 20 GPT 
# day_number = int(input('Введіть число (день): '))
# month_number = int(input('Введіть число (місяць): '))
# if 0 < day_number < 32 and 0 < month_number < 13:
#     if day_number == 31 and month_number == 12:
#         print('Новий рік завтра!')
#     elif day_number == 1 and month_number == 1:
#         print('Новий рік був учора!')
#     elif day_number == 5 and month_number == 1:
#         print('Сьогодні мій день народження!')
#     else:
#         print(f'Сьогодні: {day_number}.{month_number}')      
# else:
#     print('Перевірте дату дня, місяця')
