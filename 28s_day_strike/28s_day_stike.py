import math
import random

import values
# arr = random.sample(range(2, 16), 10)
# print(arr)
# target_num = int(input('Введіть число для пошуку: '))
# def linary_search(array: list, target: int) -> int:
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return -1
# found_index = linary_search(arr, target_num)
# print(f'Число {target_num} в масиві має індекс: {found_index}' if found_index != -1
#       else f'Число {target_num} в масиві не знайдено! Спробуйте ще раз')


# b1 = {'a1': 2, 'a2': 5, 'a3': 10}
# print(b1)
# print(type(b1))
# a1 = [2, 4, 5, 6]
# a2 = ['som', 'karp', 'schuka']
# c = dict(zip(a2, a1))
# print(c)
# print('som' in c)
# print(c.get('som'))


# a = {'інформатика': 11, "фізика": 10, "історія": 12}
# a['історія'] = 9
# print(a)
# print(f'Фізика =', a['фізика'])
# print(f'Історія =', a['історія'])
# print('фізика' in a)
# print(f'Значення ключа інформатика - {a.get("інформатика")}')
# print(f'Значення ключа хімія - {a.get("хімія")}')

# a = [1024, 1009, 1039, 1051]
# b = ['Мюнхен', "Париж", "Мюнхен", "Прага"]
# c = dict(zip(a, b))
# print(c)
# c.pop(1051)
# c.update({1066: 'Рим'})
# print(c)
# print(len(c))
# b = list(c.values())                                        
# print(f'Кількість рейсів до Мюнхена - {b.count("Мюнхен")}')


# c = {"рис": 23, "борошно": 11, "цукор": 13}
# print(c)
# c.update({'банани': 29})
# print(c)
# print(len(c))


# a = {23: "Львів", 7: "Одеса", 15: "Харків"}
# a.update({37: "Херсон", 29: "Полтава"})
# a.pop(15)
# print(a)
# print(len(a))
# print(25 in a)


# a = ['Інформатика', "Географія", "Історія", "Хімія"]
# b = [45, 53, 40, 47]
# c = dict(zip(a,b))
# print(f'Ціна підручника з хімії: {c["Хімія"]}')
# print(f'максимальна ціна підручника складає: {max(c.values())} грн.')
# print(f'Мінімальна ціна за підручник складає: {min(c.values())} грн.')

# gas_value = int(input('Введіть ціну на газ: '))
# c = {"газ": gas_value, "опалення": 1200, "телефон": 62, "електроенергія": 120}
# c.update({'холодна вода': 70})
# print(f'Ціна на газ становить: {c["газ"]}, на телефон: {c["телефон"]}')
# print(f'Оплата за телебачення відсутня' if "телебачення" not in c
#       else f'Оплата за телебачення складає: {c["телебачення"]}')
# print(f'Загальна сума ЖКХ складає: {sum(c.values())} ')


# subject = "Біологія", "Фізика", "Історія", "Математика"
# amount = 50, 60, 55, 70
# library_books = dict(zip(subject, amount))
# print(library_books)
# print(f'Загальна кількість примірників складає: {sum(library_books.values())}')


# flight_number = 2040, 3089, 1590, 2070
# flight_values = 2200, 2300, 2000, 2350
# flight_dict = dict(zip(flight_number, flight_values))
# print(flight_dict)
# min_value = min(flight_dict.values())

# Знаходимо ключ словника за його значенням
# min_flight_number = [k for k, m in flight_dict.items() if m == min_value][0]
# print(f'мінімальна ціна рейсу становить: {min_value}, номер рейсу: {min_flight_number}')

# a = [1, 2, 3, 4, 5]
# values.multiply_array(a)

# a = 1, 2, 3
# print(type(a))
# c = list(a)
# print(c, type(c))

# c = 3 - math.pi
# print(round(c, 2))

# def cone_size() -> None:
#     height = int(input('Введіть висоту конуса: '))
#     radius = int(input('Введіть радіус основи конуса: '))
#     print(f'Обєм конуса з висотою: {height}, та радіусом в основі: {radius} становить: '
#           f'{(math.pi * (pow(radius,2)) * height) / 3} см кубічних')

# cone_size()

# first_triangle = list([int(input('1трик.Введіть значення першого катета: ')), int(input('1трик.Введіть значення другого катета: '))])
# second_triangle = list([int(input('2трик.Введіть значення першого катета: ')), int(input('2трик.Введіть значення другого катета: '))])
# circle_radius = int(input('Введіть значення радіусу кола: '))

# def some_size_figures(array1: list, array2: list, radius: int) -> None:
#     print(f'Площа першого трикутника з катетами {array1[0]}, {array1[1]} дорівнює = {(array1[0]*array1[1]) / 2} см квадратних')
#     print(f'Площа другого трикутника з катетами {array2[0]}, {array2[1]} дорівнює = {(array2[0]*array2[1]) / 2} см квадратних')
#     print(f'Площа кола з радіусом {radius} буде дорівнювати: {round(math.pi * pow(radius, 2), 2)} см квадратних')

# some_size_figures(first_triangle, second_triangle, circle_radius)


# numbers_list = [3, 5, 2, 7]
# numbers_tuple = (4, 1, 5, 6)

# def math_actions(a: int, b: int, c: int, d: int) -> float:
#     result = (a*b) - (c/d)
#     return result

# print('')
# print(f'Значення виразу a*b - c/d для списку {numbers_list} буде дорівнювати {round(math_actions(*numbers_list), 2)}')
# print(f'Значення виразу a*b - c/d для кортежу {numbers_tuple} буде дорівнювати {round(math_actions(*numbers_tuple), 3)}')

# array_numbers = [random.randint(2,10) for i in range(5)]

# def average_sum(array: list) -> float:
#     result = (sum(array)) / len(array)
#     return result 
# print(f'Середнє значення чисел {array_numbers} дорівнює {average_sum(array_numbers)}')

# numbers_list = [random.randint(3, 7) for i in range(3)]
# print(numbers_list)

# def sum_factorials(array: list):
#     sum = 0
#     fact_num1 = 1
#     for i in range(2, array[0] + 1):
#         fact_num1 *= i
#     fact_num2 = 1
#     for i in range(2, array[1] + 1):
#         fact_num2 *= i
#     fact_num3 = 1
#     for i in range(2, array[2] + 1):
#         fact_num3 *= i
#     print(f'Сума факторіалів чисел {array} дорівнює {fact_num1 + fact_num2 + fact_num3}')

# sum_factorials(numbers_list)

# 1
# age = int(input('Введіть ваш вік: '))
# status = 'Дорослий' if age >= 18 else 'Неповнолітній'
# print(f'Ти - {status}')


# 2
# num = int(input('Введіть число: '))
# print(f'Число {num} - парне!' if num % 2 == 0 
#       else f'Число {num} - непарне!')


# 3
# a = int(input('Введіть число a: '))
# b = int(input('Введіть число b: '))
# print(f'Число а({a}) менше за b({b})' if a < b
#       else f'Число b({b}) менше за а({a})')


# 4
# grade = int(input('Введіть ваш бал (від 1 до 100): '))
# print(f'Відмінно!' if grade >= 90 else 'Добре' if grade >= 70 and grade < 90 else 'Погано')

# list comprehensions (Генератор списків)
# squares = [x**2 for x in range(1, 6)]
# print(squares)

# evens = [x for x in range(1, 11) if x % 2 == 0]
# print(evens)


# 1
# even_squares = [x**2 for x in range (1, 21) if x % 2 == 0]
# print(even_squares)
# max_value = max(even_squares)
# print(max_value)

# alterante option
# for i in range(len(even_squares)):
#     max_value = even_squares[0]
#     if max_value < even_squares[i]:
#         max_value = even_squares[i]
# print(max_value)


# 2. Фільтр за довжиною слова
# Є список слів: ["яблуко", "банан", "слива", "ківі", "груша"].
# За допомогою генератора створити новий список зі слів, довжина яких більше 5.
# Виведи кількість таких слів (за допомогою len()).
# Відсортуй отриманий список в алфавітному порядку та виведи.

# arr_words = ['яблуко', "банан", "слива", "ківі", "груша"]

# # добавляю елемент, тому що тільки 1 елемент виходить в новому списку
# arr_words.append('помідор')
# long_words_arr = [arr_words[x] for x in range(len(arr_words)) if len(arr_words[x]) > 5]
# print(long_words_arr)
# print(len(long_words_arr))
# long_words_arr.sort()
# print(long_words_arr)

# 3. Зміна регістру
# Є список імен: ["Оля", "Ігор", "Саша", "Марина"].
# За допомогою генератора зроби всі імена великими літерами.
# Додай до кінця списку ім’я "Катя" (операція append).
# Виведи результат.

# arr_names = ['Оля', "Ігор", "Саша", "Марина"]
# upper_names = [word.upper() for word in arr_names]
# upper_names.append('Катя'.upper())
# print(upper_names)

# 4. Перетворення температур
# Дано список температур у Цельсіях: [0, 10, 20, 30, 40].
# За допомогою генератора списку створити новий список з температурами у Фаренгейтах за формулою F = C * 9/5 + 32.
# Виведи отриманий список.
# Знайди мінімальне і максимальне значення температури у Фаренгейтах (функції min() і max()).

# arr_temperature = [0, 10, 20, 30, 40]
# farengeit_arr = [f * 9/5 +32 for f in arr_temperature]
# print(farengeit_arr)
# print(max(farengeit_arr))
# print(min(farengeit_arr))

# alternate options
# for i in farengeit_arr:
#     max_tem = farengeit_arr[0]
#     if max_tem < i:
#         max_tem = i
# print(max_tem)
# for i in farengeit_arr:
#     min_temp = farengeit_arr[0]
#     if min_temp > i:
#         min_temp = i
# print(min_temp)

# squares = {x**2 for x in random.sample(range(1,12), 11)}
# print(squares)

# even_set = {x for x in range(20) if x % 2 == 0}
# print(even_set)

# word = 'програмування'
# unique_letters = {x for x in word}
# print(unique_letters)

# fruits_list = ['kiwi', 'banana', 'kiwi', 'apple']
# lenghts = {len(x) for x in fruits_list}
# print(lenghts)

# set comprehension (генератори множин) задачки 
# Створи множину квадратів парних чисел від 1 до 20. Виведи кількість елементів у множині.
# even_squares = {x**2 for x in range (1, 21) if x % 2 == 0}
# print(even_squares)
# print(f'кількість унікальних парних вадратів - {len(even_squares)}')


# 2. Фільтрація слів за довжиною + оновлення множини
# Є список слів. Створи множину з тих, довжина яких більше 5 символів. Потім додай нове слово й видали інше.

# words = ['яблуко', 'банан', 'ківі', 'груша', 'помідор']
# lenghts_set = {x for x in words if len(x) > 5}
# lenghts_set.add('кавунище')
# lenghts_set.remove('яблуко')
# print(lenghts_set)

#  3. Знаходження спільних літер. & - перетин множин (intersection)
# Створи дві множини літер із двох слів. Знайди спільні літери між ними.

# word1 = 'програмування'
# word2 = 'градієнт'

# word3 = {ch for ch in word1} & {ch for ch in word2}
# print(word3)

# .difference() - — різниця множин для множин 
# 4. Різниця випадкових чисел
# Згенеруй дві множини з випадкових чисел у діапазоні від 1 до 10. 
# Виведи числа, які є в першій множині, але відсутні в другій.

# set1 = {random.randint(1,11) for i in range(5)}
# set2 = {random.randint(1,11) for i in range(6)}
# print(set2)
# print(set1)

# deff_set = set1 - set2
# print(f'Елементи з першої, яких немає в другої меожині: {deff_set}')

