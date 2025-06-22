import random
# 1
# Відсортуй список цілих чисел у порядку зростання методом Bubble Sort.
# arr = [5, 3, 8, 1, 2]

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for k in range(N - 1):

#         for i in range(N - 1 - k):

#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]

# bubble_sort(arr)
# print(arr)


# 2
# Відсортуй список дійсних чисел методом Selection Sort (choice sort).
# arr = [3.1, 0.5, 2.8, 1.3, 0.9]

# arr = [3.1, 0.5, 2.8, 1.3, 0.9]

# def selection_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N):
#         min_index = i

#         for k in range(min_index, N):

#             if array[k] < array[min_index]:
#                 min_index = k

#         array[i], array[min_index] = array[min_index], array[i]

# selection_sort(arr)
# print(arr)

# 3
# Відсортуй список від’ємних чисел методом Insertion Sort.
# arr = [-3, -1, -7, -4, -2]

# arr = [-3, -1, -7, -4, -2]

# def insertion_sort(array: list) -> None:
#     N = len(array)

#     for i in range(1, N):
#         k = i

#         while k > 0 and array[k] > array[k-1]:
#             array[i], array[i+1] = array[i+1], array[i]
#             k -= 1

# insertion_sort(arr)
# print(arr)

# arr = [[1, 2] for _ in range(3)]
# print(arr)

#1 Сортування цілих чисел за зростанням
# Дано список цілих чисел. Відсортуй його методом бульбашки за зростанням.

#2 Сортування цілих чисел за спаданням
# Аналогічно до попереднього, але відсортувати список за спаданням.

#3 Сортування списку з від’ємними числами
# Відсортуй список, що містить як додатні, так і від’ємні числа, за зростанням.

#4 Рахунок кількості перестановок
# Реалізуй bubble sort так, щоб додатково виводити кількість перестановок, які виконуються під час сортування.

# 🔹 Середній рівень
#5 Bubble Sort для списку з рядків
# Дано список слів (рядків). Відсортуй їх за абеткою за допомогою bubble sort.

#6 Bubble Sort без зайвих проходів
# Оптимізуй класичний алгоритм bubble sort так, щоб він завершувався раніше, якщо список уже відсортовано.

#7 Сортування за останньою цифрою
# Відсортуй список чисел за останньою цифрою кожного числа (наприклад: 12, 45, 23 → сортувати за 2, 5, 3).

# 🔹 Складніший рівень
#8 Bubble Sort для вкладеного списку
# Є список пар: [[3, 7], [1, 9], [2, 5]]. Відсортуй його за першим елементом кожної пари.

#9 Bubble Sort без використання додаткових функцій та методів списку
# Реалізуй повністю ручну версію bubble sort без використання range, len, enumerate, sorted, .sort(), тощо.

#10 Bubble Sort для списку словників
# Є список словників, наприклад:
# people = [{'name': 'Anna', 'age': 22}, {'name': 'John', 'age': 18}, {'name': 'Kate', 'age': 25}]
# Відсортуй його методом bubble sort за значенням ключа 'age'.









#1 Сортування цілих чисел за зростанням
# Дано список цілих чисел. Відсортуй його методом бульбашки за зростанням.

# arr_num = [random.randint(2, 11) for _ in range (10)]
# print(arr_num)

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N - 1):

#         for j in range(N - 1 - i):

#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]

# bubble_sort(arr_num)
# print(arr_num)

# Рекомендація (оптимізація, необов’язкова):
# Можна додати прапорець для дострокового виходу, якщо за ітерацію не було жодної перестановки:

# arr_num = [random.randint(2, 11) for _ in range (10)]
# print(arr_num)

# def bubble_sort(array: list) -> None:
#     N = len(array)

#     for i in range(N - 1):
#         swapped = False

#         for j in range(N - 1 - i):

#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#                 swapped = True
        
#         if not swapped:
#             break

# bubble_sort(arr_num)
# print(arr_num)

#2 Сортування цілих чисел за спаданням
# Аналогічно до попереднього, але відсортувати список за спаданням.
# arr_num = [random.randint(10, 25) for _ in range(8)]
# print(arr_num)

# def bubble_sort_descending(array: list) -> None:
#     N = len(array)

#     for i in range(N - 1):

#         swapped = False
#         for k in range(N - 1 - i):

#             if array[k] < array[k+1]:
#                 array[k], array[k+1] = array[k+1], array[k]
#                 swapped = True
#         if not swapped:
#             break

# bubble_sort_descending(arr_num)
# print(arr_num)

#3 Сортування списку з від’ємними числами
# Відсортуй список, що містить як додатні, так і від’ємні числа, за зростанням.

arr_num = [random.randint(-10, 10) for _ in range(12)]
print(arr_num)

