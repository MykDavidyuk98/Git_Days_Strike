import math
import random
import turtle

# bubble_sort_practise_exersice
# Вхід: [5, 2, 9, 1, 5, 6]  

# arr_number = [5, 2, 9, 1, 5, 6, 13, 25, 27]

# def bubble_sort_alg(array: list) -> None:
#     N = len(array)
#     for i in range(N-1):
#         k = i
#         swapped = False
#         for k in range(N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 swapped = True
#         if not swapped:
#             print('Масив не потребує сортировки')
#             break

# bubble_sort_alg(arr_number)
# print(arr_number)
            
# Вхід: ['banana', 'apple', 'cherry']  

# arr_words = ['banana', 'apple', 'kiwi', 'cherry']

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N-1):
#         swapped = False
#         for k in range(N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 swapped = True
#         if not swapped:
#             print('Не потрібно більше сортувати масив')

# bubble_sort(arr_words)
# print(arr_words)


# Дано список чисел.
# Відсортуй його за зростанням за допомогою bubble sort і виведи кількість обмінів, які були здійснені.
# Вхід: [3, 2, 1]  

# arr_number = [random.randint(2,18) for i in range(10)]

# def bubble_sort(array: list) -> None:
#     N = len(array)
#     waypass = 0
#     for i in range(N-1):
#         for k in range(N-1-i):
#             if array[k] > array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 waypass += 1
#     return waypass

# bubble_sort(arr_number)
# print(arr_number)

# target = int(input('Введіть число, яке потрібно знайти в ммасиві: '))

# def binary_search(array: list) -> None:
#     N = len(array)
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

# target_index = binary_search(arr_number)

# print(f'Числа немає в масиві' if target_index == -1 else f'Число {target} має індекс: {target_index}')


# Масив: [1, 3, 5, 7, 9, 11]

# arr_numbers = [1, 3, 5, 7, 9, 11]
# print(arr_numbers)
# target = int(input('Введіть число, яке потрібно знайти: '))

# def binary_search(array: list) -> None:
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

# target_index = binary_search(arr_numbers)

# print(f'Числа {target} немає в масиві' if target_index == -1 else f'Знайдено на позиції {target_index}')

# Дано відсортований список цілих чисел.
# Знайди індекс першого елемента, який не менший за задане число X. 
# Якщо такого елемента немає — виведи -1.
# Масив: [2, 4, 6, 8, 10]
# Введено: 7
# Вивід: Перший елемент ≥ 7 має індекс 3 (значення: 8)

arr_numbers = [random.randint(1, 14) for i in range(10)]
print(arr_numbers)

def insert_sort(array: list) -> None:
    N = len(array)
    for i in range (1, N):
        k = i
        while k > 0 and array[k] < array[k-1]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1

insert_sort(arr_numbers)
print(arr_numbers)

# target = int(input('Введіть число, яке потрібно знайти, та вивести перший елемент, який більший за це число: '))

# print (500 == 5e3)

# Введено: "level"
# Вивід: Це паліндром!

# word = str(input('Введіть слово на перівку його поліндрома: '))
# if word == word[::-1]:
#     print(f'Слово {word} - це поліндром')
# else:
#     print(f'Слово {word} - не поліндром')

# arr_words = ['madam', 'hello', 'racecar', 'world', 'noon']

# def if_polindrom(array: list) -> None:
#     N = len(array)
#     for i in array:
#         print(f'Слово {i} - поліндром' if i == i[::-1] else f'Слово {i} - не поліндром')

# if_polindrom(arr_words)

# def turtle_draw_S ():
#     turtle.shape('turtle')
#     turtle.forward(50)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.left(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(50)
#     turtle.right(90)
#     turtle.forward(50)

# turtle_draw_S()

# def turtle_square() -> None:
#     turtle.shape('turtle')
#     turtle.forward(75)
#     turtle.left(90) 
#     turtle.forward(75)
#     turtle.left(90)
#     turtle.forward(75)
#     turtle.left(90)
#     turtle.forward(75)
#     turtle.left(90)

# turtle_square()

# def turtle_circle() -> None:
#     turtle.shape('turtle')
#     turtle.left(90)
#     turtle.begin_fill()
#     for i in range(360):
#         if i == 180:
#             turtle.stamp()
#         turtle.forward(2)
#         turtle.left(1)
#     turtle.end_fill()

# turtle_circle()

# def turtle_ten_squares() -> None:
#     turtle.shape('turtle')
#     k = 1
#     while k < 11:
#         turtle.forward(20 + (20*k))
#         turtle.left(90)
#         turtle.forward(20 + (20*k))
#         turtle.left(90)
#         turtle.forward(20 + (20*k))
#         turtle.left(90)
#         turtle.forward(20 + (20*k))
#         turtle.left(90)
#         turtle.penup()
#         turtle.goto(-10 * k, -10 * k)
#         turtle.pendown()
#         k +=1
        
# turtle_ten_squares()

# def turtle_squares ()-> None:
#     for i in range(1,41):
#         turtle.shape('turtle')
#         turtle.forward(i * 8)
#         turtle.left(90)

# turtle_squares()

