import math
import random


# A = [0] * N_max
# n = 0
# x = int(input())
# A[n] = x
# n += 1  

# A = []
# x = int(input('Введіть число: '))
# A.append(x)
# array_length = len(A)
# x = A.pop()
# print(x)


# list comprehensions 
# A = [x**2 for x in range(10)]
# A = []
# for x in range(10):
#     A.append(x**2)
# A = [1, 2, 3, 4, 5, 6, 7]
# B = []
# for x in A:
#     if x % 2 == 0:
#         B.append(x**2)

# B = [x**2 for x in A if x % 2 == 0]
# print(B)

# Сортування вставками (insert sort)
# A = [4, 2, 5, 1, 3]
# Сортування вибором (choice sort)

def insert_sort(A:list):
    """Сортування списку A вставками"""
    N = len(A)
    for top in range (1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
    pass


def choice_sort(A: list):
    """Сортування списку А вибором"""
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]
    pass


def bubble_sort(A: list):
    """Сортування списку А  методом пузирька"""
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
    pass


def test_sort (sort_algorithm):
    print('Тестуємо: ', sort_algorithm.__doc__)
    print('testcase #1', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')


    print('testcase #2', end='')
    A = list(range(10, 20)) + list(range(0,10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')
    
     
    print('testcase #3', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')


test_sort(insert_sort)
test_sort(choice_sort)
test_sort(bubble_sort)


