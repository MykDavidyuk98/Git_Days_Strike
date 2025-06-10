import math
import random
from accessify import private, protected

# class Point:
    
#     def __new__(cls, *args, **kwargs):
#         print('Виклик __new__ для ' + str(cls))
#         return super().__new__(cls)

    
#     def __init__(self, x = 0, y = 0):
#         print(f'Виклик __init__ для {str(self)}')
#         self.x = x
#         self.y = y


# pt = Point(1, 2)
# print(pt.__dict__)
# print(pt)


# class DataBase:

#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance
        
#     def __del__(self):
#         DataBase.__instance = None

#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port
    
#     def connect(self):
#         print(f'зяднання з БД: {self.user}, {self.psw}, {self.port}')
    
#     def close(self):
#         print(f'Закриття зєднання з БД')

#     def read(self):
#         return 'Дані з БД'
    
#     def write(self, data):
#         print(f'запис в БД: {data}')

# db = DataBase('root', '1234', 80)
# db2 = DataBase('root2', '5678', 40)

# print(db2.__dict__)
# print(db.__dict__)
# print(id(db) == id(db2))

# class Vector:
#     MIN_COORD = 0
#     MAX_COORD = 100

#     @classmethod
#     def validate(cls, arg):
#         return cls.MIN_COORD <= arg <= cls.MAX_COORD


#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
    
#     def get_coords(self):
#         return self.x, self.y
    
#     @staticmethod
#     def norm2(x, y):
#         return x*x + y*y

# v = Vector(1, 2,)
# res = Vector.get_coords(v)
# print(res)
# print(Vector.validate(5))
# result = Vector.norm2(5, 6)
# print(result)

# class Point:
#     def __init__(self, x:int = 0, y:int = 0):
#         self.__x = self.__y = 0 
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y 

#     @private
#     @classmethod
#     def check_value(cls, x):
#         return type(x) in (int, float)
    
#     def set_coords(self, x, y):
#         if self.check_value(x) and self.check_value(y):
#             self.__x = x
#             self.__y = y 
#         else:
#             raise ValueError('Координати повинні бути числами')
    
#     def get_coords(self):
#         return self.__x, self.__y


# pt = Point(1, 2)
# pt.set_coords(2,4)
# print(pt.__dict__)
# print(pt.get_coords())

# pt = Point(5, 5)
# print(pt.__dict__)
# pt.set_coords(10, 10)
# pt.check_value(5)


# class Car:

#     def __init__(self, brand, year):
#         self.__brand = brand
#         self.__year = year

#     def display_info(self):
#         print(f'Brand - {self.__brand}')
#         print(f'Year - {self.__year}')


# ob1 = Car('Mustang', 1990)
# ob1.display_info()
# # ob1.__brand = 'Schevrole'
# # print(ob1._Car__brand)
# print(ob1.__dict__)
# ob1._Car__brand = 'Schevrole'
# print(ob1.__dict__)

# class Geom:
#     name = 'Geom'

#     def set_coords(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2


# class Line(Geom):
#     def draw(self):
#         print('Малювання лінії')


# class Rect(Geom):
#     def draw(self):
#         print('Малювання прямокутника')


# ob1 = Line()
# ob2 = Rect()
# ob1.set_coords(1, 2, 3, 4)
# ob2.set_coords(5, 6, 2, 8)
# print(ob1.__dict__)
# print(ob2.__dict__)


# class Cities:
    
#     def __init__(self, a1, a2):
#         self.p1 = a1
#         self.p2 = a2 
    
#     def show(self):
#         print(self.p1, self.p2)


# class Cities2(Cities):

#     def some_cities(self):
#         print('Міста України')

# ob1 = Cities2('Київ', "Вінниця")
# ob2 = Cities('Львів', "Харків")
# ob1.some_cities()
# ob1.show()
# ob2.show()


# class Math_multiply:

#    def get_numbers(self):
#        self.num1 = int(input('Введіть перше число: '))
#        self.num2 = int(input('Введіть друге число: '))
#        self.result = self.num1 * self.num2


# class Show_multiply(Math_multiply):

#     def show_mp(self):
#         print(f'{self.num1} * {self.num2} = {self.result}')

# ob1 = Show_multiply()
# ob1.get_numbers()
# ob1.show_mp()
