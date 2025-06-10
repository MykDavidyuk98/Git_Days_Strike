import math
import random

class Point:
    """Клас для представлення координат точки на системі координат Декарта

        getattr(obj, name, [, default]) - Повертає значення атрибута обєкта 
        hasattr(obj, name) - Перевірє наявність атрибуту в name в obj
        setattr(obj, name, value) - задає значення атрибуту (як що атрибут не знайдено, то він створюється )
        delattr(obj, name) - удяляє атрибут name в класі obj

        __doc__ - вміщає строку з описом класу 
        __dict__ - вміщає набір атрибутів  екземпляру класу 
    """


    color = 'red'
    circle = 2

    def __init__(self, a, b):
        print('Ініціалізація Init')
        self.x = a
        self.y = b
    
    def __del__(self):  
        print(f'Видалення екземпляру {str(self)}')


    def set_coords(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point(1, 2)
pt.set_coords(1, 2)
print(pt.__dict__)












# a = Point()
# b = Point()

# print(type(a))
# result = type(a) == Point
# print(result)

# print(isinstance(a, Point))

# Point.circle = 10
# a.color = 'grey'
# Point.type_pt = 'disc'
# setattr(Point, 'prop', 1)
# result =  getattr(Point, 'color')

# print(Point.__dict__)
# del Point.prop
# print(Point.__dict__)
 
# print(hasattr(Point, 'prop'))
# print(Point.__dict__)
# print(hasattr(Point, 'circle'))

# print(Point.__dict__)
# a.x = 1
# print(a.__dict__)
# del a.color
# print(a.__dict__)
# a.y = 2
# print(a.__dict__)
# b.x = 10
# b.y = 20
# print(b.__dict__)
# print(Point.__doc__)

# c = Point.__doc__
# print(c)

# pt = Point()
# print(pt.set_coords(1, 2))
# print(pt.__dict__)
# pt2 = Point()
# pt2.set_coords(10, 20)
# print(pt2.__dict__)
# print(pt.get_coords())

# result = getattr(pt, 'set_coords')
# print(result)
# Додай до класу Car метод display_info(), який виводить інформацію про автомобіль у форматі: "Brand: ..., Model: ..., Year: ...".


class Car:
    """Клас для створення обєктів машин з класом Car з настуними атрибутами: 
       brand - марка машини
       model - модель машини
       year - рік випуску 
    """

    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f'Brand: {self.brand}')
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')

porsche = Car('Porsche', 'Coyot', 2001)
mustang = Car("Mustang", 'GT', 1969 )
print(porsche.__dict__)
print(mustang.__dict__)
print(Car.__doc__)
porsche.display_info()
mustang.display_info()