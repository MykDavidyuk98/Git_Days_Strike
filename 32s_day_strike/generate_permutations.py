import math
import random

# def find(number, A):
#     """шукає x in a повертає True якщо такий є 
#         False як що такого немає"""
    
#     flag = False
#     for x in A:
#         if number == x:
#             return True
#             break
#     return flag


# def generate_numbers(N: int, M: int, prefix = None):
#     """Гунерує всі числа (з лідующими нулями, які нічого не значат, в
#         N - річній системі зчислення (N <= 10), довжини M)"""

#     prefix = prefix or []

#     if M == 0:
#         print(prefix)
#         return 
    
#     for digit in range(N):
#         prefix.append(digit)
#         generate_numbers(N, M-1, prefix)
#         prefix.pop()

# # generate_numbers(4, 3)


# def gen_bin(M, prefix=''):

#     if M == 0:
#         print(prefix)
#         return

#     for digit in '0', '1':
#         gen_bin(M-1, prefix+digit)

# # gen_bin(5)

# def generate_permutations(N: int, M: int = -1, prefix = None):
#     """Генерація всіх перестановок N чисел в M позиціях
#         починаючи з префіксом (prefix)"""
    
#     M = N if M == -1  else M
#     prefix = prefix or []

#     if M == 0:
#         print(*prefix)
#         return
    
#     for number in range(1, N+1):
#         if find (number, prefix):
#             continue
#         prefix.append(number)
#         generate_permutations(N, M-1, prefix) 
#         prefix.pop()

# generate_permutations(3)


# Рекурентні(рекурсивні) сортировки:

# Швидка сортировка Тоні Хоара (W(N*log*N)) до O(N**2)
# Виконує сортувальні дії, виконується на прямому ході рекурсії
# Виконується без додаткової памяті 
# входить до алгоритмів "розділяй та володарюй"
# барєрний елемент



# Сортировка Слиянием (Злиттям) (O(N * log*N)) 
# Виконується на зворотньому ході рекурсії 
# Потрібна додаткова память (O(N)) додаткової памяті


# class K18_01:
#     a = 'Oukey'
# ob1 = K18_01()
# ob2 = K18_01()
# print(ob1.a)
# print(ob2.a)

# class K01_01:
#     a = 'інформатика'
#     b = 'фізика'
# ob1 = K01_01()
# ob2 = K01_01()

# print(ob1.a)
# print(ob2.b)
