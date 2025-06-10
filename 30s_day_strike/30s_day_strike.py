import math
import random

# print('Будемо грати в вікторину!')

# playing = str(input('Хочеш зіграти?: '))
# print(playing)

arr_numbers = [4, 7, 6, 5, 8, 3]

def insertion_sort(array: list) -> None:
    N = len(array)

    for i in range(1, N):
        k = i

        while k > 0 and array[k] < array[k-1]:
            array[k], array[k-1] = array[k-1], array[k]

insertion_sort(arr_numbers)
print(arr_numbers)