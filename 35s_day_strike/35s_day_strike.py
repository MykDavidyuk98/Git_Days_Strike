import math
import random

# class Point:
#     circle = 2
#     color = 'red'

#     def __init__(self, y, x: int = 0):
#         self.x = x
#         self.y = y


#     def __del__(self):
#         print(f'Видалення екземпляру {self}')


#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
    

#     def get_coords(self):
#         return self.x, self.y


# pt = Point(y=1)
# print(pt.__dict__)

# class K17_05:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# pt = K17_05("Вивчаємо", "інформатику")
# print(pt.__dict__)
# print(pt.x, pt.y)
  
# class Countries:

#     def __init__(self, x = 'Владік', y = 'в попу гадік'):
#         self.x = x
#         self.y = y

# pt = Countries("Коля")
# pt2 = Countries(y = 'і Коля')
# pt3 = Countries('Женя', "і Владік")
# print(pt.x, pt.y)
# print(pt2.x, pt2.y)
# print(pt3.x, pt3.y)

# class Fotball_teams:

#     def __init__(self, a1, a2, a3):

#         self.p1 = a1
#         self.p2 = a2
#         self.get_group(a3)
    

#     def get_group(self, a3):

#         if a3 <= 4:
#             self.p3 = '- перша група'
#         elif 4 < a3 < 9:
#             self.p3 = '- друга група'
#         elif 9 < a3 < 13:
#             self.p3 = '- третя група'      
#         else:
#             self.p3 = '- четверта група'

# ob1_target = random.randint(0, 16)
# ob1 = Fotball_teams('Реал', "Мадрид", ob1_target)

# ob2_target = random.randint(0, 16)
# ob2 = Fotball_teams('Манчестер', "Юнайтед", ob2_target)

# ob3_target = random.randint(0, 16)
# ob3 = Fotball_teams('Шахтар', "Донецьк", ob3_target)

# ob4_target = random.randint(0, 16)
# ob4 = Fotball_teams('Динамо', "Київ", ob4_target)

# print(ob1.p1, ob1.p2, ob1.p3)
# print(ob2.p1, ob2.p2, ob2.p3)
# print(ob3.p1, ob3.p2, ob3.p3)
# print(ob4.p1, ob4.p2, ob4.p3)


# class Constructor:

#     def __init__(self, a1, a2, a3):
#         self.p1 = a1
#         self.p2 = a2
#         self.p3 = a3
#         print(f'{self.p1} {self.p2} {self.p3}')

# first = Constructor(a2= '- столиця', a1= 'Київ', a3= 'України')


# class Math_pow:

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.sum = (pow(self.a, 2) + pow(self.b, 2)) / 2
#         print(f'Значення виразу ({self.a}² + {self.b}²) / 2 = {self.sum}')

# num_a = int(input('Введіть значення змінної a: '))
# num_b = int(input('Введіть значення змінної b: '))

# first = Math_pow(num_a, num_b)


# class Some_constructor_print:

#     def __init__(self, a1 = 'Дністер', a2 = 'Десна'):
#         self.p1 = a1
#         self.p2 = a2
#         print(f'Перший аргумент - {self.p1}, другий - {self.p2}')

# ob1 = Some_constructor_print('Дніпро', "Ворскла")
# ob2 = Some_constructor_print('Дніпро')
# ob3 = Some_constructor_print()
        

# class Math_op:
#     def __init__(self, a1= 3, a2= 4):
#         self.a1 = a1
#         self.a2 = a2
#         self.sum = self.a1 * self.a2
#         print(f'{self.a1} * {self.a2} = {self.sum}')

# ob1 = Math_op()
# ob2 = Math_op(5, 6)
# ob3 = Math_op(7)


# class Math_op:

#     def __init__(self, a1, a2):

#         self.a1 = a1
#         self.a2 = a2

#         print(f'{self.a1} * {self.a2} = {self.a1 * self.a2}' if a1 > a2 
#               else f'{self.a1} / {self.a2} = {self.a1 / self.a2}')
        
# first_num = random.randint(1, 10)
# second_num = random.randint(1, 10)

# ob1 = Math_op(first_num, second_num)
# ob2 = Math_op(3, 63)


# class OS_system:

#     def __init__(self, a1= 'Операційна', a2= 'система'):

#         self.a1 = a1
#         self.a2 = a2
#         self.a3 = str(input('Введіть назву ОС: ').strip().lower())

#         print(f'{self.a1} {self.a2} {self.a3.capitalize()}' if self.a3 == 'linux'
#               else f'{self.a1} {self.a2} Windows')

# ob1 = OS_system()
        
# class Point:

#     def __new__(cls, *args, **kwargs):
#         print('Виклик __new__ для' + str(cls))
    
#     def __init__(self, x, y):
#         print('виклик __init__ для ' + str(self))
#         self.x = x
#         self.y = y
        
        





        