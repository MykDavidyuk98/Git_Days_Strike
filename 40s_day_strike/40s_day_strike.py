import math
import random

from accessify import private, protected
from typing import Union

# 1
# def is_string(a1: str) -> bool:
#     """Перевіряє чи обєкт є рядком(str)"""

#     return isinstance(a1, str)

# some_object = 'qwerty'
# print(is_string(some_object))
# some_object2 = 235
# print(is_string(some_object2))


# 2
# def is_number(a1: Union[float, int]):
#     """Перевіряє чи обєкт є числом (int / float)"""
#     return isinstance(a1, (float, int))

# some_object = 3.25
# print(is_number(some_object))
# print(type(some_object))

# some_object = 25
# print(is_number(some_object))
# print(type(some_object))

# some_object = 'qwerty'
# print(is_number(some_object))
# print(type(some_object))


# 3
# data = [1, 'hi', 2.5, [1, 2], 'cat', 3]

# def filter_list(array: list) -> list:
#     N = len(array)
    # new_list = []

    # for i in range(N):
    #     if isinstance(array[i], (int, float)):
    #         new_list.append(array[i])
    # return new_list
            
    # alterante option
    # return [x for x in array if isinstance(x, (float, int))]

# filter_data = filter_list(data)
# print(filter_data)


# 4
# a = int(input('введіть число a: '))
# b = int(input('введіть число b: '))

# def safe_add(a: Union[int, float], b: Union[int, float]):
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     else:
#         return 'Invalid input'

# print(safe_add(a, b))
# print(safe_add('a', b))

# 5
# arr = ['some', 'kiwi', 5, 10, [1, 5, 7], {'name': 'olia', 'class': 5}, {'name': 'Vasia', 'class': 4}]
# count_str = len([x for x in arr if isinstance(x, str)])
# count_dict = len([x for x in arr if isinstance(x, dict)])
# count_list = len([x for x in arr if isinstance(x, list)])
# print(count_str)
# print(count_dict)
# print(count_list)


# 6
# class Animal:
#     def __init__(self):
#         pass

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()

# class Cat(Animal):
#     def __init__(self):
#         super().__init__()

# def is_animal(object):
#     return isinstance(object, (Animal))

# ob1 = Dog()
# ob2 = 'string'
# ob3 = Cat()
# ob4 = Animal()

# some_dict = [ob1, ob2, ob3, ob4]
# for i in some_dict:
#     print(is_animal(i))


# 7
# def type_check(value):
#     if isinstance(value, str):
#         return 'string'
#     elif isinstance(value, (int, float)):
#         return 'Number'
#     elif isinstance(value, list):
#         return 'List'
#     else:
#         return 'Unknown'

# ALTERNATE_OPTION
# def type_check(value):
#     return type(value).__name__.upper()

# a = 5
# print(type_check(a))
# b = 'text' \
# 'dsfdsf'
# print(type_check(b))
# c = [1, 10, 12]
# print(type_check(c))
# d = {5, 1, 10, 9}
# print(type_check(d))


#8
# class K_01:

#     def __init__(self, a1, a2):
#         self.p1 = a1
#         self.p2 = a2 

#     def func1_add(self):
#         return self.p1 + self.p2
    
#     def func2_mul(self):
#         return self.p1 * self.p2
    

# class K_01a(K_01):

#     def func3_sub(self):
#         return self.p1 - self.p2
    
# class K_01b(K_01):

#     def func4_dec(self):
#         return self.p1 / self.p2

# ob1 = K_01a(16, 7)
# print(f'Операції над обєктом {str(ob1)}')
# print(ob1.func1_add())
# print(ob1.func2_mul())
# print(ob1.func3_sub())

# ob2 = K_01b(16, 7)
# print(f'Операції над обєктом {ob2}')
# print(ob2.func1_add())
# print(round(ob2.func4_dec(), 2))


# 9
# class Parent:

#     def __init__(self, a1, a2):
#         self.p1 = a1
#         self.p2 = a2
#         print(f'Створено обєкт з атрибутами "{self.p1}", "{self.p2}"')
    
#     def make_list(self):
#         return list(str(self.p1))
    
#     def exclusion(self, a2):
#         # Добавив a2 - можливість використовувати метод до любого значення при беспосередньому виклику метода
#         self.a2 = a2
#         return self.a2[slice(0, -1)]

# class Child(Parent):

#     def concat(self):
#         self.p3 = self.p1 + self.p2
#         return self.p3
    
#     def exclusion(self, a2):
#         # Добавив a2 - можливість використовувати метод до любого значення при беспосередньому виклику метода
#         return super().exclusion(a2) + ' Перевизначення методу в дочірньому класі'
    
# first = 'екземпляр'
# second = 'підкласу'

# ob1 = Child(first, second)
# print(ob1.concat())
# print(ob1.make_list())
# print(ob1.exclusion(second))
# print(ob1.exclusion('secondiry'))

# 10
# arr = [random.randint(2, 15) for x in range(3)]
# arr2 = [5, 6, 'some']

# class Main:

#     def __init__(self, *args):
#         if not all(isinstance(x, (int, float)) for x in args):
#             raise TypeError ('Усі аргументи мають бути цілими числами int або дійсними числами float')
#         self.p1 = list(args)

#     def average(self):
#         return f'Середнє значення суми 3х чисел = {round((sum(self.p1)) / len(self.p1), 2)}'
    
# class Sub_Main(Main):

#     def average(self):
#         return 'Перевизначення методу до батьківського класу Main. ' + super().average()
    
# print(f'Початкове значення масиву: {arr}')

# ob1 = Sub_Main(*arr)
# print(ob1.average())

# # Перевірка елементів на тип данних в масиві 
# ob2 = Sub_Main(*arr2)

# 11
# class Shape:

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         pass

#     def area(self):
#         return 'Площа не визначена'

# class Rectangle(Shape):

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         super().__init__(width, height)
    
#     def area(self):
#         if not all(isinstance(x, (int, float)) for x in (self.width, self.height)):
#             raise TypeError ('Параметрам потрібно надати значення int або float')
#         return f'Площа прямокутника {round(self.width * self.height, 2)}'
    
# class Circle(Shape):

#     def __init__(self, radius):
#         if isinstance(radius, (int, float)):
#             self.radius = radius
#         else:
#             raise TypeError('Радіус потрібно задати типом int / float')

#     def area(self):
#         return f'Площа кола - {round(math.pi * pow(self.radius, 2), 2)}'
        
# ob1 = Rectangle(11.3, 22.5)
# print(ob1.area())

# ob2 = Circle(15)
# print(ob2.area())

# ob3 = Shape(10, 15)
# print(ob3.area())


# 12
# class Worker:

#     def calculate_salary(self):
#         return 'Базова зарплата'
    

# class HourlyWorker(Worker):

#     def __init__(self, hours, rate):
#         if all(isinstance(x, (int, float)) for x in (hours, rate)):
#             self.hours = hours
#             self.rate = rate
#         else:
#             raise TypeError('hours and rate must be int / float')
    
#     def calculate_salary(self):
#         return f'Ставка погодинного працівника за {self.hours} годин складає - {self.hours * self.rate:.2f}'


# class FixedWorker(Worker):

#     def __init__(self, monthly_rate):
#         if isinstance(monthly_rate, (int, float)):
#             self.monthly_rate = monthly_rate
#         else:
#             raise TypeError('monthly_rate must be int / float')
    
#     def calculate_salary(self):
#         return f'Ставка штатного працівника - {self.monthly_rate:.2f}'


# ob1 = Worker()
# ob2 = HourlyWorker(12, 5)
# ob3 = FixedWorker(120)

# arr_workers = [ob1, ob2, ob3]

# for x in arr_workers:
#     print(x.calculate_salary())

# 13
# class Transport:

#     def move(self, distance):
#         if isinstance(distance, (int, float)):
#             self.distance = distance
#             return f'Рух транспортного засобу на {self.distance}м'
#         else:
#             raise TypeError('distance must be int / float')

# class Car(Transport):
#     def move(self, distance):
#         if isinstance(distance, (int, float)):
#             self.distance = distance
#             return f'Рух машини на {self.distance * 0.001}км'
#         else:
#             raise TypeError('distance MUST be int / float')
        
# class Bicycle(Transport):
#     def move(self, distance):
#         if isinstance(distance, (int, float)):
#             self.distance = distance
#             return f'Рух велосипеда на {self.distance * 100}см'
#         else:
#             raise TypeError('distance must be INT / FLOAT')

# ob1 = Transport()
# print(ob1.move(100))

# ob2 = Car()
# print(ob2.move(int('2000')))

# ob3 = Bicycle()
# print(ob3.move(int("1000")))

# 14
# class Shape:

#     def area(self):
#         return 'Площа не визначена'


# class Rectangle(Shape):

#     def __init__(self, width, height):
#         if all(isinstance(x, (int, float)) for x in (width, height)):
#             self.width = width
#             self.height = height
#             self.size = self.width * self.height
#         else:
#             raise TypeError('width and height must be int / float')
        
#     def area(self):
#         return f'Площа прямокутника - {self.size:.1f}'
        
        

# class Triangle(Shape):
#     def __init__(self, base, height):
#         if all(isinstance(x, (int, float)) for x in (base, height)):
#             self.base = base
#             self.height = height
#             self.size = base * height * 0.5
#         else:
#             raise TypeError('base and height must be int / float')
        
#     def area(self):
#         return f'Площа трикутника - {self.size:.1f}'
        

# class Circle(Shape):

#     def __init__(self, radius):
#         if isinstance(radius, (int, float)):
#             self.radius = radius
#         else:
#             raise TypeError('radius must be int, float')

#     def area(self):
#             return f'Площа кола - {math.pi * pow(self.radius, 2):.1f}'
        

# ob1 = Shape()
# ob2 = Rectangle(10, 5)
# ob3 = Triangle(10, 5)
# ob4 = Circle(5)

# geom = [ob1, ob2, ob3, ob4]
# for i in geom:
#     print(i.area())

# 15
# class Order:
#     __global_item_list = []

#     def calculate_order(self):
#         return 0
    
#     def add_item(self, item):
#         self.item = item.capitalize()
#         self.__global_item_list.append(self.item)
    
#     @classmethod
#     def get_item_list(cls):
#         return cls.__global_item_list

# class OnLineOrder(Order):

#     def __init__(self, amount):
#         self.__amount = amount
    
#     def calculate_order(self):
#         return f'Сума онлайн замовлення - {self.__amount * 1.1:.1f}грн'

# class InStoreOrder(Order):

#     def __init__(self, amount):
#         self.amount = amount
    
#     def calculate_order(self):
#         return f'Сума завмовлення в магазині - {self.amount}грн'
    

# ob1 = Order()
# ob2 = OnLineOrder(100)
# ob3 = InStoreOrder(200)

# arr = [ob1, ob2, ob3]

# for i in arr:
#     print(i.calculate_order())

# ob1.add_item('Computer')
# ob2.add_item('microwave')
# ob3.add_item('mouse')

# print(Order.get_item_list())

# 16
# class Employee:

#     def __init__(self, rate):
#         if isinstance(rate, (int, float)) and rate > 0:
#             self.rate = rate
#         else: 
#             raise TypeError('rate must be > 0 and must be int / float')

#     def get_salary(self):
#             return 'Не вказано'
    
# class HourlyEmployee(Employee):

#     def get_salary(self):
#         return f'ЗП погодиного працівника - {self.rate}'

# class SalariedEmployee(Employee):
     
#     def get_salary(self):
#         return f'ЗП штатного працівника - {self.rate}'


# ob1 = Employee(100)
# ob2 = HourlyEmployee(1000)
# ob3 = SalariedEmployee(1500)

# arr= [ob1, ob2, ob3]

# for i in arr:
#     print(i.get_salary())


# 17
# class Instrument:

#     def play(self):
#         return 'Start playing'


# class Guitar(Instrument):

#     def play(self):
#         return super().play() + ' by Guitar'

# class Drum(Instrument):

#     def play(self):
#         return super().play() + ' by Drum'

# class Piano(Instrument):

#     def play(self):
#         return super().play() + ' by Piano'


# ob1 = Instrument()
# ob2 = Guitar()
# ob3 = Drum()
# ob4 = Piano()

# arr = [ob1, ob2, ob3, ob4]

# for i in arr:
#     print(i.play())

