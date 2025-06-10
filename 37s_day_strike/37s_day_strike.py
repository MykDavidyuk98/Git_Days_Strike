import math
import random

from accessify import private, protected

# class Math_op:

#     def __init__(self, a1, a2, a3):
#         self.p1 = a1
#         self.p2 = a2
#         self.p3 = a3
    
#     def sum_math(self):
#         self.sum_res = self.p1 + self.p2 + self.p3
    
#     def product_math(self):
#         self.product_res = self.p1 * self.p2 * self.p3
    

# class Math_op2(Math_op):

#     def diff_math(self):
#         self.diff_res = (self.p1 + self.p2) - self.p3
    
#     def show(self):
#         print(f'Сума - {self.sum_res}\nДобуток - {self.product_res}\nРізниця - {self.diff_res}')


# ob1 = Math_op2(5, 10, 5)
# ob1.sum_math()
# ob1.product_math()
# ob1.diff_math()
# ob1.show()

# class Triangle_size:

#     def __init__(self, a1, a2):
#         self.p1 = a1
#         self.p2 = a2
    
#     def triangle_size(self):
#         self.ts = (self.p1 * self.p2) / 2
    

# class Show_size(Triangle_size):

#     def show_size(self):
#         print(f'Площа трикутника - {self.ts}')


# ob1 = Show_size(5, 5)        
# ob1.triangle_size()
# ob1.show_size()

# ob2 = Show_size(12, 6)
# ob2.triangle_size()
# ob2.show_size()


# class Grades:

#     def __init__(self, a1, a2, a3):
#         self.p1 = a1
#         self.p2 = a2
#         self.p3 = a3
    
#     def average(self):
#         aver = (self.p1 + self.p2 + self.p3) / 3
#         return round(aver, 1)


# class Student(Grades):

#     def show(self):
#         print(f'Середнє арифметичне {self.p1}, {self.p2}, {self.p3} - {self.average()}')

# vasia = Student(10, 8, 4)
# vasia.average()
# vasia.show()


# class BankAccount: 

#     def __init__(self, a1):
#         self.__balance = a1
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print('Недостатньо коштів!')
#         else:
#             self.__balance -= amount
    
#     def show_balance(self):
#         print(f'Баланс - {self.__balance}')

# ob1 = BankAccount(1000)
# ob1.show_balance()
# ob1.deposit(100)
# ob1.withdraw(2000)
# ob1.show_balance()

# class Person:

#     def __init__(self, name):
#         self._name = name
    
# class Employee(Person):

#     def show_name(self):
#         print(f'імя - {self._name}')

# ob1 = Employee('Richard')
# ob1.show_name()


# class Rectangle:

#     def __init__(self, a, b):
#         self.p1 = a
#         self.p2 = b
    
#     def area(self):
#         area = self.p1 * self.p2
#         return area

#     def perimeter(self):
#         perimeter = (self.p2 + self.p1) * 2       
#         return perimeter

# class Square(Rectangle):

#     def info(self):
#         if self.p1 == self.p2:
#             print(f'Квадрат зі стороню {self.p1}, площа - {self.area()}, периметр - {self.perimeter()}')
#         else:
#             print('Не квадрат')

# ob1 = Square(5, 5)
# ob1.info()


# class Book:

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
    
#     def info(self):
#         print(f'Назва - {self.title}, автор - {self.author}')
    

# class FictionBook(Book):

#     def genre_info(self, genre):
#         self.genre = genre
#         print(f'Жанр - {self.genre}')

# ob1 = FictionBook('Mody Dick', 'Herman Melville' )
# ob1.info()
# ob1.genre_info('adventure')


# class Person:

#     def __init__(self, name):
#         self._name = name
    
# class Employee(Person):

#     def get_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary
#         else:
#             print('ЗП має бути додатня')

#     def show_employee(self):
#         print(f'імя - {self._name}, зарплата - {self.__salary}')

# pers1 = Employee('Kolia')
# pers1.get_salary(50000000)
# pers1.show_employee()
# print(pers1._Employee__salary)
# Хочеш — можемо ускладнити: додати кілька працівників, підрахувати загальну зарплату або перевірити тип даних.
        

# class SecretAccount:

#     def __init__(self, code):
#         self.__code = code
    
#     def check_code(self, guess):
#         if guess == self.__code:
#             print('Авторизацію пройдено')
#         else:
#             print('Пароль невірний!')

# ob1 = SecretAccount('89togopi')
# ob1.check_code('89togopi')
# Якщо хочеш ускладнити задачу — додай лічильник спроб або обмеження.


# class Rectangle:

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def area(self):
#         area = self.a * self.b
#         return area
    
#     def perimeter(self):
#         per = (self.a + self.b) * 2
#         return per
    
# class ShapeCheck(Rectangle):
#     def check(self):
#         if self.a == self.b:
#             print(f'Квадрат. Площа - {self.area()}, периметр - {self.perimeter()}')
#         else:
#             print(f'Прямокутник не квадарт. Площа - {self.area()}, периметр - {self.perimeter()}')

# rect = ShapeCheck(8, 812)
# rect.check()


# class Point:
#     MAX_COORD = 100
#     MIN_COORD = 0

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def set_coords(self, x, y):
#         if self.MIN_COORD <= x <= self.MAX_COORD:
#             self.x = x
#             self.y = y
    
#     def __getattribute__(self, item):
#         if item == 'x':
#             raise ValueError('Доступ заборонено')
#         else:
#             return object.__getattribute__(self, item)
    
#     def __setattr__(self, key, value):
#         if key == 'z':
#             raise AttributeError('Недопустиме значення атрибуту')
#         else:
#             object.__setattr__(self, key, value)
    
#     def __getattr__(self, item):
#         return False        
    
#     def __delattr__(self, name):
#         print('__delattr__: ' + name)
#         object.__delattr__(self, name)

# pt1 = Point(1, 2)
# pt2 = Point(10, 20)
# del pt1.x
# print(pt1.__dict__)

# class User:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __getattribute__(self, item):
#         print(f'Отримано доступ до атрибута: {item}')
#         return object.__getattribute__(self, item)

# ob1 = User(5, 10)
# res = ob1.x
# res2 = ob1.y
# print(res)
# print(res2)

# class BankAccount:
    
#     def __init__(self, balance):
#         self.balance = balance
    
#     def __setattr__(self, name, value):
#         print(f'Баласнс оновлено: нове значення - {value}')
#         super().__setattr__(name, value)

# ob1 = BankAccount(1000)
# ob1.__setattr__('balance', 15000)


# class Product:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __getattribute__(self, name):
#         print(f'Атрибут {name} - {object.__getattribute__(self, name)}')
#         return object.__getattribute__(self, name)

#     def __getattr__(self, item):
#         return f'Атрибута {item} не існує'

# ob1 = Product(5, 10)
# print(ob1.x)
# print(ob1.zz)


# class Student:

#     def __init__(self, name):
#         self.name = name
    
#     def __delattr__(self, name):
#         print(f'Імя {name} видалено з класу Student')
#         super().__delattr__(name)

# ob1 = Student('Igor')
# print(ob1.__dict__)
# del ob1.name
# print(ob1.__dict__)


# class Logger:
    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __getattribute__(self, name):
#         print(f'Звертання до атрибуту: {name}')
#         return super().__getattribute__(name)

# ob1 = Logger(10, 8)
# ob1.x
# print(ob1.y)
        

# class Temperature:

#     def __init__(self, celsius):
#         self.__celsius = celsius

#     def set_att(self, celsius):
#         self.__celsius = celsius

#     def __setattr__(self, name, value):
#         print(f'Значення оновленно: {value}')
#         super().__setattr__(name, value)

# ob1 = Temperature(10)
# ob1.set_att(20)
# ob1.set_att(25)
# ob1._Temperature__celsius = 8
# print(ob1.__dict__)


# class Cleaner:

#     def __init__(self, name, role):
#         self.name = name
#         self.role = role
    
#     def __delattr__(self, name):
#         print(f'Атрибут {name} видалено')
#         super().__delattr__(name)
        
# ob1 = Cleaner('Kolia', 'pitcher')
# ob1.__delattr__('name')
# print(ob1.__dict__)
# ob1.__delattr__('role')
# print(ob1.__dict__)


# class Account:

#     def __init__(self, balance):
#         self.balance = balance
    
#     def __setattr__(self, name, value):
#         if name == 'balance' and value < 0:
#             print(f'Баланс не може бути відємним!')
#         else:
#             print(f'Встановлення {name} - {value}')
#             super().__setattr__(name, value)

# ob1 = Account(1000)
# ob1.balance = -5
# ob1.balance2 = -10


# class Profile:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def __getattribute__(self, name):
#         if name in ('x', 'y', '__dict__'):
#             return super().__getattribute__(name)
#         return f'Атрибут {name} не підтримується! Перевірте допустимість атрибутів'

# ob1 = Profile(5, 10)
# print(ob1.x)
# print(ob1.role)
# print(ob1.__dict__)

# ✅ Завдання 5: Квадрати чисел
# 📌 За допомогою map() і lambda створи список квадратів чисел.
# 🔹 Список: [1, 2, 3, 4, 5]

# func1 = lambda x : abs(x)
# print(func1(-9))

# alterante option
# func2 = lambda x: x if x >= 0 else - x
# print(func2(12))

# func3 = lambda x: True if x % 2 == 0 else False
# print(func3(4))
# print(func3(16))
# print(func3(5))

# Alternate option:
# func4 = lambda x: x % 2 == 0
# print(func4(4))
# print(func4(7))
# print(func4(18))

# arr_words = ['siriuz', 'banana', 'apple', 'cherry', 'kiwi']
# func5 = sorted(arr_words, key=lambda word: word[-1])
# print(func5)

# arr_numbers = [4, 11, 32, 5, 9, 15]
# func6 = list(filter(lambda x: x > 10, arr_numbers))
# print(func6)


# arr_numbers = [1, 2, 3, 4, 5]
# func7 = list(map(lambda x: x*x, arr_numbers))
# print(func7)

