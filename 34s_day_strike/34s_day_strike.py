import math
import random


# class Point:
#     color = 'red'
#     circle = 2 


#     def __init__(self, x = 0, y = 0):
#         print('Виклик __init__')
#         self.x = x
#         self.y = y


#     def __del__(self):
#         print(f'Видалення екземляру {str(self)}')


#     def set_coords(self, x, y):
#         self.x = x 
#         self.y = y 


#     def get_coords(self):
#         return (self.x, self.y)
    
    
# pt = Point(y = 1)
# print(pt.__dict__)


# class K17_03:
#     predm = 'інформатика'
#     klas = 8

#     def set_predm(self, a1):
#         self.predm = a1

#     def set_klas(self, a2):
#         self.klas = a2
    
# ob1 = K17_03()
# ob2 = K17_03()

# print(ob1.predm, ob1.klas)
# print(ob2.predm, ob2.klas)

# ob1.set_predm('математика')
# ob2.set_predm('історія')
# ob2.set_klas(9)
# print(ob1.predm, ob1.klas)
# print(ob2.predm, ob2.klas)


# class Predmet:
#     a1 = 'інформатика'
#     a2 = 'фізика'

# first = Predmet()
# second = Predmet()

# print(first.a1)
# print(second.a2)

# class Country:
#     a = 'Україна'
#     b = 'Франція'

# first = Country()
# second = Country()
# num = int(input('Введіть ціле число: '))

# print(f'Число більше 5: {first.a}' if num > 5 
#       else f'Число менше або рівне 5: {second.b}')


# class Temp:
#     a1 = 'байт'

#     def get_a1(self):
#         print(f'Виконується метод для обєкта {self}, виводимо змінну: {self.a1}')

# first = Temp()
# second = Temp()

# first.get_a1()
# second.get_a1()

# class Temp:
#     value = ''

#     def show_value(self):
#         print(f'Значення виведенної змінної: {self.value}')

    

# first = Temp()
# second = Temp()

# first.value = 'файл'
# second.value = 'папка'

# first.show_value()
# second.show_value()

# class Math_methods:

#     def set_multiply(self, x):
#         self.x = x
#         print(f'Сума множення: {self.x * 8}')
    
#     def set_divine(self, y):
#         self.y = y
#         print(f'Сума ділення: {self.y / 9}')

# a1 = Math_methods()
# a2 = Math_methods()

# a1.set_multiply(x = 10)
# a2.set_divine(y = 81)
import math

class Math_operations:

    def size_circle(self, r):
        self.r = r
        print(f'Обєм кулі радіуса {r} = {(4/3) * math.pi * pow(self.r, 3)}')
    
    def size_triangle(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.p = (self.a + self.b + self.c) / 2
        print(f'Площа трикутника зі сторонами {self.a}, {self.b}, {self.c} = {math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))} ')
    
a1 = Math_operations()
a1.size_circle(10)
a1.size_triangle(10, 15, 12)