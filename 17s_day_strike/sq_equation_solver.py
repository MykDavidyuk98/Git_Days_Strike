import math
import random
from math import sqrt   

def _calculate_d(a: float, b: float, c: float) -> float:
    return b ** 2 - 4 * a * c


def solve_equation(a: float, b: float, c: float) -> float:
    d = _calculate_d(a, b, c)
    print(f'Equation {a} * x  ^ 2 + {b} * x + {c}  = 0')

    if d > 0 :
        x1 = (-b - sqrt(d) / (2*a))
        x2 = (-b + sqrt(d) / (2*a))
        print(f'Two roots, x1 = {x1}, x2 = {x2}')
    elif d == 0:
        x = -b / (2 * a)   
        print(f'One root: x = {x}')
    else:   
        print('No roots')
solve_equation(4, 3, -1)
a = 4
b = 3 
c = -1

