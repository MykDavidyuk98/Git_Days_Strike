import math
import random

def array_search(A: list, N: int, x: int):
    """Виконує пошук числа X в масиві A в діапазоні від 0
    до N - 1 індекса не включно. 
    Повертає індекс елемента X в масиві A
    Або -1 як о такого немає 
    Яко в масиві декілька одинакових елементів , рівних X , вернути 
    індекс першого по рахунку
    """
    for k in range(N):
        if A[k] == x:
            return k
    return - 1

def test_array_search(): 
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print('#test1 - ok')
    else: 
        print('#test1 - fail')


    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print('#test2 - ok')
    else: 
        print('#test2 - fail')


    A2 = [10, 20, -3, -4, -5]
    m = array_search(A2, 5, 10)
    if m == 0:
        print('#test3 - ok')
    else: 
        print('#test3 - fail')

def invert_array(A: list, N: int):
    """ Зміна масиву (спераду на на кінець)
        в рамках індексу 0 до N - 1
    """
    pass

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    invert_array(A1, 5)
    if A1 == [5, 4, 3, 2, 1]:
        print('#test1 - ok') 
    else: 
        print('#test1 - fail')

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    invert_array(A2, 5)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print('#test2 - ok') 
    else: 
        print('#test2 - fail')