import math
import random
# mas = ['Kolia', 'Dina', 'Sacha', 'Maks', 'Olia']
# for i in range(len(mas)):
#     print(mas[i], end=' ')

# mas = []
# n = int(input('Введіть довжину масиву: '))
# a = int(input('Введіть число a: '))
# b = int(input('Введіть число b: '))
# for i in range(n):
#     a *= b
#     mas.append(a)
# for i in range(n):
#     print(mas[i])

# mas = []
# num_of_el = int(input('Введіть кількість елементів: '))
# for i in range (num_of_el):
#     b = int(input(f'Введіть {i}й елемент:'))
#     mas.append(b)
#     print(mas)
# sum_of_elements = 0
# for i in range (num_of_el):
#     sum_of_elements += mas[i]
# print(sum_of_elements)
# print(num_of_el)
# sum_of_elements /= num_of_el
# print(f'Середнє значення елементів масиву = {sum_of_elements}')

# num_of_el = int(input('Введіть кількість елементів: '))
# mas = []
# for i in range(num_of_el):
#     b = str(input(f'Введіть {i+1} елемент:'))
#     mas.append(b)
# print(mas, sep= ':')

# mas = []
# len_mas = int(input('Введіть кількість елементів масиву: '))
# for i in range(len_mas):
#     new_num = int(input(f'Введіть {i+1} елемент: '))
#     mas.append(new_num)
# print(mas)

# el_mas = 10
# mas = []
# for i in range(el_mas):
#     b = random.randint(4, 10)
#     mas.append(b)
#     print(f'В масив додано елемент: {b}')       # перевірка добавлення елементу 
# mas = [random.randint(4,10) for i in range (el_mas)]
# print(mas)

# el_num = 5
# mas = []
# step = 4
# first_el = 3
# mas.append(first_el)
# for i in range(el_num-1):
#     first_el += step
#     mas.append(first_el)
# print(mas)

# alternate option
# mas = [3 + 4 * i for i in range(5)]
# print(mas)


# length_mas = 7
# mas = [random.randint(2, 6) for i in range (length_mas)]
# print(mas)          # Перевірка масиву
# sum_el = sum(mas)
# print(sum_el)       # вивід суми елементів масиву 

# mas = []
# sum_elements = 0
# mas_length = 7
# for i in range(mas_length):
#     b = random.randint(2, 6)
#     mas.append(b)
# print(mas)          # Перевірка масиву
# for i in range(mas_length):
#     sum_elements += mas[i]
# print(sum_elements)          # вивід суми елементів масиву 

# task 6 st62. 
# mas = [3]
# first_el = 3
# length_mas = 6 
# prog_denominator = 2
# sum_of_el = 0
# for i in range(length_mas-1):
#     first_el *= prog_denominator
#     mas.append(first_el)
# print(mas)
# print(sum(mas)/length_mas)

# 💡 Альтернативний (коротший) варіант:
# mas = [3 * 2**i for i in range(6)]
# print(mas)
# print(sum(mas) / len(mas))

# mas = [random.randint(2, 9) for i in range(12)]
# print(mas)
# b = 0
# for i in range(len(mas)):
#     if mas[i] == 5:
#         b += 1
#         print(f'Елемент {mas[i]} знаходиться на позиції {i+1} його кількість {b}')

# приклад пошуку елемента в ВІДСОРТОВАНОМУ масиві двійковим методом 
# mas = [1, 4, 5, 2, 8, 10, 12, 15]
# mas = sorted(mas)
# print(mas)
# left = 0
# right = len(mas) - 1
# target = 10
# found = False 
# for i in range(len(mas)):
#     mid = (left + right) // 2
#     print(f'Перевіряємо середину: {mid}')
#     if mas[mid] == target:
#         print(f'Знайдено {target} на позиції {mid}')
#         found = True 
#         break
#     elif mas[mid] < target:
#         left = mid + 1
#     else:
#         right = mid + 1
# if not found:
#     print(f'число {target} не знайдене')

# mas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# left = 0 
# right = len(mas) -1 
# target = 3
# found = False
# for i in range(len(mas)):
#     mid = (left + right)//2
#     if mas[mid] == target:
#         print(f'Заєбісь {target} на позиції {mid}')
#         found = True
#         break
#     elif mas[mid] > target:
#         right = mid + 1
#     else:
#         left = mid - 1
# if not found:
#     print('немає')

# mas = [6, 8, 13, 17, 19, 30]
# found = False
# left = 0 
# right = len(mas) - 1
# target = 17
# for i in range(len(mas)):
#     mid = (left + right) // 2
#     if mas[mid] == target:
#         print(f'Заєбісь, {target} на позиції {mid}')
#         found = True
#         break
#     elif mas[mid] > target:
#         right = mid - 1
#     else:
#         left = mid + 1
# if not found:
#     print('fuck it')


# mas_length = int(input('Введіть кількість елементів масиву: '))
# mas = []
# for i in range(mas_length):
#     new_el = int(input(f'Введіть {i+1} елемент: '))
#     mas.append(new_el)
# mas = sorted(mas)
# print(mas)          # Перевірка створеного масиву       
# target = int(input('Введіть число для пошуку: '))
# left = 0
# right = len(mas) - 1
# flag = False
# for i in range(len(mas)):
#     mid = (left + right) //2
#     if mas[mid] == target:
#         print(f'Знайдено {target} на позиції {mid+1}, індекс елемента в масиві {mid}')
#         flag = True
#         break
#     elif mas[mid] > target:
#         right = mid -1
#     else:
#         left = mid +1
# if not flag:
#     print('Елемента не знайдено!!!')

# mas = [random.randint(1, 50) for i in range(10)]
# mas = sorted(mas)
# print(f'Згенерований масив чисел: {mas}')
# target = int(input('Введіть число для пошуку: '))
# left = 0
# right = len(mas) - 1
# flag = False
# for i in range(len(mas)):
#     mid = (left + right) // 2
#     if mas[mid] == target:
#         print(f'Знайдено {target} на позиції {mid+1} з індексом {mid}')
#         flag = True
#         break
#     elif mas[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if not flag:
#     print(f'Елемента {target} не знайдено!!!')




# Генерація випадкового масиву
# mas = [random.randint(1, 50) for i in range(10)]
# mas = sorted(mas)
# print(f'Згенерований масив чисел: {mas}')

# Введення цілі для пошуку
# target = int(input('Введіть число для пошуку: '))

# Бінарний пошук через while
# left = 0
# right = len(mas) - 1
# found = False

# while left <= right:
#     mid = (left + right) // 2
#     if mas[mid] == target:
#         print(f'Знайдено {target} на позиції {mid + 1}, індекс: {mid}')
#         found = True
#         break
#     elif mas[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# if not found:
#     print(f'Елемента {target} не знайдено!')

# mas = [random.randrange(0, 101,2) for i in range(15)]
# mas = sorted(mas)
# print(f'Відсортований масив: {mas}')
# target = int(input('Введіть число, яке потрібно знайти: '))
# left = 0
# right = len(mas) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2 
#     if mas[mid] == target:
#         print(f'Число {target} знайдено !!! Його порядкова позиція {mid+1}, індекс: {mid} ')
#         found = True
#         break
#     elif mas[mid] < target:
#         left = mid + 1
#     else: 
#         right = mid - 1
# if not found:
#     print(f'Число {target} не знайдене!!!')

# mas = [random.randrange(2, 101, 2) for i in range (30)]
# mas = sorted(mas)
# print(f'Масив має вигляд: {mas}')
# target = int(input('Введіть число для пошуку: '))
# left = 0
# right = len(mas) - 1
# found = False
# while left <= right:
#     mid = (left + right) // 2
#     if mas[mid] == target:
#         count_target = 0
#         found = True
#         print(f'Число {target} має позицію {mid+1} (індекс: {mid})')
#         break
#     elif mas[mid] < target:
#         left = mid +1
#     else:
#         right = mid - 1
# if not found:
#     print(f'Число {target} не знайдене')

# mas = ['байт', "принтер", "процесор", "монітор"]
# target = "принтер"
# for i in range(len(mas)):
#     if mas[i] == target:
#         print(f'рядок "{target}" розташовано на позиції {i+1}')

# альтернативний код .index() method 
# print(f'Рядок "{target}" розташовано на позиції {mas.index(target)+1}')

# mas = [13, 7, 6, 7, 9, 7]
# target = 7
# count_target = 0
# found = False
# for i in range(len(mas)):
#     if mas[i] == target:
#         count_target += 1
#         found = True
# if not found:
#     print(f'Число {target} не зустрічається в масиві')
# else:
#     print(f'Число {target} в масиві зустрічається {count_target} разів')

# mas = ["блок", "файл", "біт", "колонка", "миша"]
# # max_element = max(mas)
# # min_element = min(mas)
# # print(max_element)
# # print(min_element)

# # 2й варіант
# max_el = mas[0]
# min_el = mas[0]
# for i in range (len(mas)):
#     if max_el < mas[i]:
#         max_el = mas[i]
#     if min_el > mas[i]:
#         min_el = mas[i]
# print(max_el, min_el)

# mas = [random.randint(3, 9) for i in range (10)]
# count =  mas.count(6)
# print(mas)
# if count != 0:
#     print(f'Число 6 є в списку, зустрічається {count} разів')
# else: 
#     print(f'Числа 6 в списку немає')

# другий варіант 
# mas = [random.randint(3, 9) for i in range (10)]
# print(mas)
# count = 0
# index_list = []
# for i in range(len(mas)):
#     if mas[i] == 6:
#         count += 1
#         new_index = i + 1
#         index_list.append(new_index)
# if count != 0:
#     print(f'Число 6 є в списку, зустрічається під такими номерами {index_list} ')

# mas = [96, 34, 11, 105, 24]
# min_el = mas[0]
# max_el = mas[0]
# for i in range(len(mas)):
#     if min_el > mas[i]:
#         min_el = mas[i]
#     if max_el < mas[i]:
#         max_el = mas[i]
# print(f'у масиві {mas} максимальний елемент {max_el} з позицією {mas.index(max_el) + 1}(індекс: {mas.index(max_el)})')
# print(f'Мінімальний елемент {min_el}, з позицією {mas.index(min_el)+ 1}(індекс: {mas.index(min_el)})')

# mas = [96, 34, 11, 105, 24]
# min_el = min(mas)
# max_el = max(mas)
# print(f'у масиві {mas} максимальний елемент {max_el} з позицією {mas.index(max_el) + 1}(індекс: {mas.index(max_el)})')
# print(f'Мінімальний елемент {min_el}, з позицією {mas.index(min_el)+ 1}(індекс: {mas.index(min_el)})')

# Вивести суму чисел від 1 до N
# Користувач вводить число N, програма виводить суму всіх чисел від 1 до N включно.
# end_number = int(input('Введіть число по яке потрібно порахувати суму чисел від 1: '))
# sum_number = 0 
# for i in range(1, end_number+1, 1):
#     sum_number += i
# print(sum_number)

# Вивести всі парні числа від 1 до N
# Користувач вводить число N, програма виводить усі парні числа в діапазоні.
# end_num = int(input('Введіть число: '))
# for i in range(2, end_num+1, 2):
#     print(i)

# Обчислити факторіал числа за допомогою while
# Факторіал — добуток усіх цілих чисел від 1 до N.