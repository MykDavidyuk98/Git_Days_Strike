import math
import random

def find(number, A):
    """шукає x in a повертає True якщо такий є 
        False як що такого немає"""
    
    flag = False
    for x in A:
        if number == x:
            return True
            break
    return flag


def generate_numbers(N: int, M: int, prefix = None):
    """Гунерує всі числа (з лідующими нулями, які нічого не значат, в
        N - річній системі зчислення (N <= 10), довжини M)"""

    prefix = prefix or []

    if M == 0:
        print(prefix)
        return 
    
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

# generate_numbers(4, 3)


def gen_bin(M, prefix=''):

    if M == 0:
        print(prefix)
        return

    for digit in '0', '1':
        gen_bin(M-1, prefix+digit)

gen_bin(5)

def generate_permutations(N: int, prefix: None, M: int = -1):
    """Генерація всіх перестановок N чисел в M позиціях
        починаючи з префіксом (prefix)"""
    
    M = N if M == -1  else M
    prefix = prefix or []

    if M == 0:
        print(prefix)
        return
    
    for number in range(1, N+1):
        if find(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix) 
        prefix.pop()

       